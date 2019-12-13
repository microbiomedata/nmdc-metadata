%.py: %.yaml
	pipenv run gen-py-classes $< > $@.tmp && mv $@.tmp $@
