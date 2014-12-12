"""
max_to_cookie
=============

Usage
-----

    max_to_cookie.py <project_path> <stem_name>

Where:

    <project>: Name of the project directory that is generated using the MaxIDE.
    <stem_name>: Value of one of the fields in the project creation dialogue. At the moment, for simplicity, we do not support override of naming options. 

About
-----

This is a quick and dirty script I have written for automatically creating cokiecutter templates out of regular MaxCompiler project. You can find out more about
cookiecutter [here](https://github.com/audreyr/cookiecutter). 

The logic of project creation which has been automated in this script is based on reverse-engineering - I generated a few project by selecting various options,
and diff-ed the project folders to get an idea of what went on behind the scenes. As a result, the correctness of this script is questionable at the moment.

"""

import os, sys
import shutil

project = sys.argv[1]
stem = sys.argv[2]

# try and copy the cpu code template with all the slic interfaces
print 'Copying CpuCode template...'
shutil.copyfile(os.path.join('./templates', 'CpuCode.c'), os.path.join('./' + project, 'CPUCode/' + stem + 'CpuCode.c'))
print 'Done.'

# try and copy the manager code template with standard as well as custom manager
print 'Coping ManagerCode template...'
shutil.copyfile(os.path.join('./templates', 'Manager.maxj'), os.path.join('./' + project, 'EngineCode/src/' + stem.lower() + '/' + stem + 'Manager.maxj'))
print 'Done.'

# try and replace project name with context variable
print 'Replacing project name with {{cookiecutter.project_name}}...'
os.system('grep -rl %s ./ | xargs sed -i "s/%s/{{cookiecutter.project_name}}/g"' % (project, project))
print 'Done.'

#try and replace {{cookiecutter.dfe_model}} with context variable
print 'Replacing {{cookiecutter.dfe_model}} with {{cookiecutter.dfe_model}}...'
os.system('grep -rl {{cookiecutter.dfe_model}} ./ | xargs sed -i "s/{{cookiecutter.dfe_model}}/{{cookiecutter.dfe_model}}/g"')
print 'Done.'

# try and replace stem name with context variable
print 'Replaceing given stem name with {{cookiecutter.stem_name}}'
os.system('grep -rl %s ./ | xargs sed -i "s/%s/{{cookiecutter.stem_name}}/g"' % (stem, stem))
print 'Done.'

# try and replace stem name lower with context variable
print 'Replacing given stem name (lowercase) with {{cookiecutter.stem_name|lower}}...'
os.system('grep -rl %s ./ | xargs sed -i "s/%s/{{cookiecutter.stem_name|lower}}/g"' % (stem.lower(), stem.lower()))
print 'Done.'

# try and replace the mpcx setting with context variable
print 'Replacing enableMPCX setting with template logic...'
os.system('grep -rl "<enableMPCX enabled=\\"false\\"/>" ./ | xargs sed -i "s@<enableMPCX enabled=\\"false\\"/>@<enableMPCX enabled=\\"{% if cookiecutter.optimize_for_mpcx %}true{% else %}false{% endif %}\\"/>@g"')
print 'Done.'

# try and rename all the files now
print 'Replacing files names containing stem name with {{cookiecutter.stem_name}}...'
for root, dirs, files in os.walk("./" + project):
    for x in files:
       if stem in x:
            os.rename(os.path.join(root, x), os.path.join(root, x.replace(stem, '{{cookiecutter.stem_name}}')))
print 'Done.'

# try and rename all the directories
print 'Replacing directory names containint stem name (lowercase) with {{cookiecutter.stem_name|lower}}'
for root, dirs, files in os.walk("./" + project):
    for x in dirs:
       if stem.lower() in x:
            os.rename(os.path.join(root, x), os.path.join(root, x.replace(stem.lower(), '{{cookiecutter.stem_name|lower}}')))
print 'Done.'

# try and rename the whole project folder
print 'Renaming project folder...'
os.rename('./' + project, '{{cookiecutter.project_name}}')
print 'Done.'
