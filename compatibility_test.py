import os
from pygeppetto.model import CompositeType, StateVariableType, SimpleArrayType, ArrayType
from pygeppetto.model.types import ImportType
from pygeppetto.model.utils import pointer_utility
from pygeppetto.model.values import ImportValue, StringArray, Pointer,TimeSeries

from nwb_explorer import nwb_model_interpreter
from nwb_explorer.nwb_data_manager import get_file_from_url, NWBDataManager
from nwb_explorer.nwb_model_interpreter import NWBModelInterpreter, GeppettoModelAccess
import pynwb
from pynwb import NWBHDF5IO

# TODOs: test sweeptable, processing and image series
# TODOs: how to store the test results?
# TODOs: how to incorporate this with nwb_update_readme.py ?
def test_nwbe_compatibility(nwbfile_path):
    # test acquisition and stimulus
    name = os.path.basename(nwbfile_path)
    io = NWBHDF5IO(nwbfile_path, mode='r', load_namespaces=True)
    nwbfile=io.read()
    count = 0
    acquisition_var = []
    for a, v in nwbfile.acquisition.items():
        acquisition_var.append(a)
        count += 1
        if count == 3:
            break
    # start testing
    test_lvl = []
    try:
        # file_path = get_file_from_url(file_url=file_path, fname=name, cache_dir=tmpdir)
        nwb_interpreter = NWBModelInterpreter(nwbfile_path)
        geppetto_model = nwb_interpreter.create_model()
        geppetto_model_access = GeppettoModelAccess(geppetto_model)
        variable_type = geppetto_model.variables[0].types[0]
        imported_type = nwb_interpreter.importType('DUMMY', 'nwbfile', variable_type.eContainer(),
                                                   geppetto_model_access)
        geppetto_model_access.swap_type(variable_type, imported_type)
        print('File read correctly:', name)
        test_lvl.append('1')

    except Exception as e:
        print('Error reading file', e.args)

    for a, v in nwbfile.acquisition.items():
        if count ==0:
            pass
        elif count <=2:
            test_result_timestamps = _test_importValue(geppetto_model,nwb_interpreter,a,'timestamps')
            test_result_data = _test_importValue(geppetto_model, nwb_interpreter, a, 'data')
        else:
            break
        count += 1

def _test_importValue(geppetto_model, nwb_interpreter, acquisition_var, acquisition_var_type):
    var_to_import = pointer_utility.find_variable_from_path(geppetto_model,
                                                            'nwbfile.acquisition.' + acquisition_var + '.'+acquisition_var_type)
    value = var_to_import.initialValues[0].value
    assert type(value), ImportValue
    value = nwb_interpreter.importValue(value)
    assert type(value) == TimeSeries
    return test_result