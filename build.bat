rmdir /Q /S build dist
call py36 setup.py sdist bdist_wheel
py36 -m twine upload dist/*