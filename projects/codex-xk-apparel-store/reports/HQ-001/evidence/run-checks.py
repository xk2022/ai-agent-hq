import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

base = Path('/workspace/scratch/HQ-001-1qnZaIVi')
source = base / 'source'
work = base / 'test-copy'
evidence = Path('/workspace/ai-agent-hq/projects/codex-xk-apparel-store/reports/HQ-001/evidence')
if not work.exists():
    shutil.copytree(source, work, ignore=shutil.ignore_patterns('.git'))
(base / 'npm-cache').mkdir(exist_ok=True)
files = subprocess.check_output(['git', '-C', str(source), 'ls-files', '-z']).decode().split('\0')
command = ['bwrap', '--ro-bind', '/', '/', '--tmpfs', '/workspace', '--tmpfs', '/home', '--tmpfs', '/root', '--tmpfs', '/tmp', '--proc', '/proc', '--dev', '/dev', '--dir', '/workspace/work', '--bind', str(work), '/workspace/work', '--bind', str(base / 'npm-cache'), '/workspace/cache']
for filename in files:
    if filename:
        command += ['--ro-bind', str(work / filename), '/workspace/work/' + filename]
mode = sys.argv[1]
if mode not in ('prepare', 'audit'):
    command += ['--unshare-net']
command += ['--chdir', '/workspace/work']
if mode == 'prepare':
    args = ['npm', 'ci', '--ignore-scripts']
elif mode == 'audit':
    args = ['npm', 'audit', '--json']
elif mode == 'install':
    # Cache was populated without lifecycle scripts; install hook stays offline.
    args = ['npm', 'ci', '--offline', '--no-audit', '--no-fund']
elif mode == 'test':
    args = ['npm', 'test']
elif mode == 'coverage':
    args = ['node', '--test', '--test-isolation=none', '--experimental-test-coverage', '--test-coverage-include=dist/assets/*.js', *[str(p.relative_to(work)) for p in sorted((work / 'tests').glob('*.test.mjs'))]]
else:
    raise SystemExit('unknown mode')
allowed = {'PATH', 'HTTP_PROXY', 'HTTPS_PROXY', 'NO_PROXY', 'http_proxy', 'https_proxy', 'no_proxy', 'NODE_EXTRA_CA_CERTS', 'SSL_CERT_FILE', 'SSL_CERT_DIR'}
env = {k: v for k, v in os.environ.items() if k in allowed}
env.update({'npm_config_cache': '/workspace/cache', 'npm_config_userconfig': '/dev/null', 'npm_config_globalconfig': '/tmp/hq-empty-global.npmrc', 'npm_config_update_notifier': 'false'})
start = datetime.now(timezone.utc).isoformat()
result = subprocess.run(command + args, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=240)
log = evidence / ('npm-' + mode + '.log')
log.write_text(result.stdout)
summary = {'phase': mode, 'command': args, 'cwd_inside_sandbox': '/workspace/work', 'host_copy': str(work), 'revision': subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip(), 'started_at': start, 'finished_at': datetime.now(timezone.utc).isoformat(), 'exit_code': result.returncode, 'tracked_files_read_only_mounts': True, 'network_isolated': mode not in ('prepare', 'audit'), 'environment': 'allowlist only; no auth variables; user/global npm configs disabled', 'log': log.name}
(evidence / ('npm-' + mode + '.json')).write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
print(result.stdout[-12000:])
raise SystemExit(result.returncode)
