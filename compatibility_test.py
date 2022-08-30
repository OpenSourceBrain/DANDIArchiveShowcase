import sys
from nwb_explorer.nwb_model_interpreter import NWBModelInterpreter, GeppettoModelAccess
# TODOs: test sweeptable, processing and image series
def test_nwbe_compatibility(nwbfile_path):

    nwb_interpreter = NWBModelInterpreter(nwbfile_path)
    geppetto_model = nwb_interpreter.create_model()
    geppetto_model_access = GeppettoModelAccess(geppetto_model)
    variable_type = geppetto_model.variables[0].types[0]
    imported_type = nwb_interpreter.importType('DUMMY', 'nwbfile', variable_type.eContainer(),
                                                   geppetto_model_access)
    geppetto_model_access.swap_type(variable_type, imported_type)
#
#     for a, v in nwbfile.acquisition.items():
#         if count ==0:
#             pass
#         elif count <=2:
#             test_result_timestamps = _test_importValue(geppetto_model,nwb_interpreter,a,'timestamps')
#             test_result_data = _test_importValue(geppetto_model, nwb_interpreter, a, 'data')
#         else:
#             break
#         count += 1
#
# def _test_importValue(geppetto_model, nwb_interpreter, acquisition_var, acquisition_var_type):
#     var_to_import = pointer_utility.find_variable_from_path(geppetto_model,
#                                                             'nwbfile.acquisition.' + acquisition_var + '.'+acquisition_var_type)
#     value = var_to_import.initialValues[0].value
#     assert type(value), ImportValue
#     value = nwb_interpreter.importValue(value)
#     assert type(value) == TimeSeries
#     return test_result

if __name__ == '__main__':
    test_nwbe_compatibility(sys.argv[1])