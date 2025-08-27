def select_backend(method, req, settings):
    # Honor explicit tier, else infer from policy
    if hasattr(req, 'tier') and req.tier:
        return req.tier
    # Infer from router.yaml policies
    policies = settings.ROUTER_POLICIES
    if method in policies['infer_tier']['task_kind']:
        return policies['infer_tier']['task_kind'][method]
    if getattr(req, 'needs_index', False):
        return 'large'
    return policies['default_tier']
