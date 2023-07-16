'''
This function is meant to be called from nwb_table_readme.py script to test NWBE compatibility
'''
import sys


def test_nwbe_compatibility(nwbfile_path,docker_arg):
    if(docker_arg):
    	try:
    		sys.path.insert(0, '/home/jovyan/nwb-explorer/nwb_explorer')
		from nwb_model_interpreter import NWBModelInterpreter, GeppettoModelAccess
	except ImportError:
		print("NWBE docker container not setup as the program expects")
    else:
    	from nwb_explorer.nwb_model_interpreter import NWBModelInterpreter, GeppettoModelAccess	
    nwb_interpreter = NWBModelInterpreter(nwbfile_path)
    geppetto_model = nwb_interpreter.create_model()
    geppetto_model_access = GeppettoModelAccess(geppetto_model)
    variable_type = geppetto_model.variables[0].types[0]
    imported_type = nwb_interpreter.importType('DUMMY', 'nwbfile', variable_type.eContainer(),
                                                   geppetto_model_access)
    geppetto_model_access.swap_type(variable_type, imported_type)

if __name__ == '__main__':
    test_nwbe_compatibility(sys.argv[1])
    test_nwbe_compatibility(sys.argv[2])
