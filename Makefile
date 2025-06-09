# Minimal makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

help:
	@echo "Copy paste this:"
	@echo ""
	@echo "python -m venv .venv"
	@echo "source .venv/bin/activate"
	@echo "make livehtml"
	@echo "open http://127.0.0.1:8000"
	@echo ""

# Live reload for development
livehtml: clean
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)
	@echo "Serving HTML on http://127.0.0.1:8000"

# Put it first so that "make" without argument is like "make html"
html:
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$READTHEDOCS_OUTPUT/html" $(SPHINXOPTS) $(O)

# Clean build files
clean:
	rm -rf $(BUILDDIR)/*

# Catch-all target: route all unknown targets to Sphinx
%: Makefile
	$(SPHINXBUILD) -b $@ "$(SOURCEDIR)" "$(BUILDDIR)/$@" $(SPHINXOPTS) $(O)

.PHONY: help html clean livehtml Makefile
    