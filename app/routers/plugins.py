from fastapi import APIRouter, Request

router = APIRouter(prefix="/plugins", tags=["Plugins"])


@router.post("/{plugin_name}/execute")
def run_plugin(plugin_name: str, payload: dict, request: Request):
    loader = request.app.state.plugin_loader
    return loader.execute(plugin_name, payload)