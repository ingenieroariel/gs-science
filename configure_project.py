"""Install and configure all requirements for running the gs-science project
from the git repository.

This is specific to Ubuntu. If you don't use Ubuntu, you must do the steps manually.

It is assumed that ssh keys have been set up at github.com and that git repository has been cloned e.g. using the command

git clone git@github.com:ingenieroariel/gs-science.git



"""

# Manual steps:
# python-pip does not exist in Ubuntu < Karmic, so one must get it manually from
# http://pypi.python.org/packages/source/p/pip/pip-0.7.2.tar.gz
# unpack in install with distutils: python setup.py install



import os
def run(cmd, 
        stdout=None,
        stderr=None, 
        verbose=True):
        
    s = cmd    
    if stdout:
        s += ' > %s' % stdout
        
    if stderr:
        s += ' 2> %s' % stderr        
        
    if verbose:
        print s
    err = os.system(s)
    
    if err != 0:
        msg = 'Command "%s" failed with errorcode %i. ' % (cmd, err)
        if stderr: msg += 'See logfile %s for details' % stderr
        raise Exception(msg)


def install_ubuntu_packages():    
    """Get required Ubuntu packages for geoserver.
       It is OK if they are already installed
    """

    print('Installing Ubuntu packages')     
    
    s = 'sudo apt-get clean'
    run(s, verbose=True)
    
    for package in ['python-setuptools']: #, 'python-pip']: # Pip not in Ubuntu pre-Karmic
    #for package in ['python-setuptools', 'python-pip']:

                    
        s = 'sudo apt-get -y install %s' % package
        
        log_base = '%s_install' % package
        try:
            run(s,
                stdout=log_base + '.out',
                stderr=log_base + '.err',                  
                verbose=True)
        except:
            msg = 'Installation of package %s failed. ' % package
            msg += 'See log file %s.out and %s.err for details' % (log_base, log_base)
            raise Exception(msg)
            
            
#def clone_repository():
#    """Get project from git repository.
#    """
#    
#    s = 'git clone %s' % repository
#    run(s)
    
def setup_environment():
    """Configure project enviroment
    """
    
    s = 'sudo easy_install pip'
    run(s)
    
    s = 'sudo pip install -r requirements.txt'
    run(s)


    
if __name__ == '__main__':

    install_ubuntu_packages()
    setup_environment()


