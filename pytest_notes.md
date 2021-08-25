# Pytest

## Options

- ```-k``` Expression only run tests which match the given substring expression
  ``` pytest -k "test_method or other" ```
- ```-m```  only run tests matching given mark expression.
- ```-x```  exit instantly on first error or failed test.
- ```--maxfail=2``` exit after first num failures or errors.
- ```--lf``` rerun only the tests that failed last time
- ```--ff``` run all tests but run the last failures first
- ```-v``` verbosity ```-q```
- ```-l``` show locals
- ```-tb``` traceback
- ```--collect-only``` only collect, not run

## Examples

```bash
 1053  pytest -m "smoke and not get" --collect-only
 1054  pytest
 1055  pytest -x
 1056  pytest --maxfail=2
 1057  pytest --maxfail=1
 1058  pytest
 1059  pytest --lf
 1060  pytest --ff
 1061  pytest -v
 1062  pytest -q
 1063  pytest -l
 1064  pytest --tb=no
 1065  pytest --tb=line
 1066  pytest --durations=3
 1067  pytest --durations=3
 1068  pytest --durations=3 -vv