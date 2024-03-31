@echo off
echo Running extract.py...
python extract.py
echo extract.py completed.

echo Running articles.py...
python articles.py
echo articles.py completed.

echo Running verify.py...
python verify.py
echo verify.py completed.

echo Running separate.py...
python separate.py
echo separate.py completed.

echo Running publish.py...
python publish.py
echo publish.py completed.

echo All scripts completed.
pause
