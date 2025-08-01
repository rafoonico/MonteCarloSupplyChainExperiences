import io
import importlib.util
import sys
from pathlib import Path

def load_app():
    package_path = Path(__file__).resolve().parents[1] / 'app'
    module_path = package_path / '__init__.py'
    spec = importlib.util.spec_from_file_location('app_pkg', module_path, submodule_search_locations=[str(package_path)])
    module = importlib.util.module_from_spec(spec)
    sys.modules['app_pkg'] = module
    spec.loader.exec_module(module)
    return module.create_app()

def test_upload_latin1_csv():
    app = load_app()
    client = app.test_client()
    csv_content = 'demand,produto\n1,Água\n2,Leite\n'
    data = {
        'file': (io.BytesIO(csv_content.encode('latin1')), 'test.csv'),
        'periods': '1'
    }
    response = client.post('/', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b'Forecast and Inventory Parameters' in response.data