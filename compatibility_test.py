'''
This function is meant to be called from nwb_table_readme.py script to test NWBE compatibility
'''
import sys
import argparse
import datetime
from multiprocessing import Process
        
def limit_time(func, args, kwargs, time):
    p = Process(target=func, args=args, kwargs=kwargs)
    p.start()
    p.join(time)
    if p.is_alive():
        p.terminate()
        return False

    return True

def test_nwbe_compatibility(nwbfile_path, docker_arg):
    if docker_arg:
        try:
            sys.path.insert(0, '/home/jovyan/nwb-explorer/nwb_explorer')
            from nwb_model_interpreter import NWBModelInterpreter,GeppettoModelAccess
        except ImportError:
            print ('NWBE docker container not setup as the program expects')
    else:
        from nwb_explorer.nwb_model_interpreter import NWBModelInterpreter, \
		    GeppettoModelAccess	    
    nwb_interpreter = NWBModelInterpreter(nwbfile_path)
    geppetto_model = nwb_interpreter.create_model()
    geppetto_model_access = GeppettoModelAccess(geppetto_model)
    variable_type = geppetto_model.variables[0].types[0]
    imported_type = nwb_interpreter.importType('DUMMY', 'nwbfile',
	        variable_type.eContainer(), geppetto_model_access)
    geppetto_model_access.swap_type(variable_type, imported_type) 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cap limit on downloaded file size')
    parser.add_argument('--test_docker', default=False, action='store_true',
                        help='test using the NWBE docker container')
    parser.add_argument('text', action='store', type=str, help='The text to parse.')
    args = parser.parse_args()
    counter = limit_time(test_nwbe_compatibility, (args.text,args.test_docker, ), {}, 100)
    if counter:
        print("created successfully!")
    else:
        print("forever")
    #test_nwbe_compatibility(args.text,args.test_docker)
    #sub-anm244024_ses-20141112_obj-jyoa6b_behavior+icephys+ogen.nwb
