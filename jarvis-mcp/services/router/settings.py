import os
yaml = None
try:
    import yaml as _yaml
    yaml = _yaml
except ImportError:
    pass

class Settings:
    RUNNER_MODE = os.getenv('RUNNER_MODE', 'lmstudio')
    LMSTUDIO_BASE_URL = os.getenv('LMSTUDIO_BASE_URL', 'http://host.docker.internal:1234')
    ROUTER_POLICIES = {
        'default_tier': 'small',
        'infer_tier': {
            'task_kind': {
                'scaffold': 'small',
                'prime': 'medium',
                'generate': 'medium',
                'review': 'medium',
                'refactor': 'large',
                'tests': 'medium',
                'plan': 'small',
                'explain': 'medium'
            },
            'needs_index': 'large'
        }
    }
    # Optionally load from configs/router.yaml
    if yaml:
        try:
            with open('configs/router.yaml') as f:
                ROUTER_POLICIES = yaml.safe_load(f)['policies']
        except Exception:
            pass
settings = Settings()
