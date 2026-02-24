# Makefile
# =========================================
# Project: Sphinx documentation for homelab
# =========================================

# --------------------------------------------------
# ⚙️ Environment Settings
# --------------------------------------------------
SHELL := /bin/bash
.SHELLFLAGS := -O globstar -c
# If V is set to '1' or 'y' on the command line,
# AT will be empty (verbose).  Otherwise, AT will
# contain '@' (quiet by default).  The '?' is a
# conditional assignment operator: it only sets V
# if it hasn't been set externally.
V ?= 0
ifeq ($(V),0)
    AT = @
else
    AT =
endif
# Detect if we are running inside GitHub Actions CI.
# GitHub sets the environment variable GITHUB_ACTIONS=true in workflows.
# We set CI=1 if running in GitHub Actions, otherwise CI=0 for local runs.
ifeq ($(GITHUB_ACTIONS),true)
CI := 1
else
CI := 0
endif
# Define a reusable CI-safe runner
define run_ci_safe =
( $1 || [ "$(CI)" != "1" ] )
endef
# --------------------------------------------------
# ⚙️ Sphinx Build Settings
# --------------------------------------------------
# You can set these variables from the command line, and also
# from the environment for the first two.
# --------------------------------------------------
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
PUBLISHDIR    ?=

# Define the directories where autosummary generates stub files
STUBDIRS      = api _autosummary_generated
# --------------------------------------------------
.PHONY: all publish-markdown help clean Makefile markdown-gen
all: markdown-gen publish-markdown

markdown-gen: markdown

ifeq ($(PUBLISHDIR),)
publish-markdown:
	$(AT)echo "⚠️  Warning: Skipping publish-markdown target because PUBLISHDIR is empty."
else
publish-markdown:
	$(AT)echo "🧹 Cleaning Previous published Sphinx artifacts..."
	$(AT)rm -rf $(PUBLISHDIR)
	$(AT)echo "✅ Finished cleaning old Sphinx artifacts."
	$(AT)echo "🚀 Publishing sphinx markdown documentation to $(PUBLISHDIR)..."
	$(AT)mkdir -p $(PUBLISHDIR)
	$(AT)mv $(BUILDDIR)/markdown/* $(PUBLISHDIR)
	$(AT)echo "✅ Finished published markdown documentation to $(PUBLISHDIR)."
endif
# --------------------------------------------------
# Help
# --------------------------------------------------
help:
	$(AT)$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
# --------------------------------------------------
# Custom clean target: removes build artifacts AND generated stub files
# --------------------------------------------------
clean:
	$(AT)echo "🧹 Cleaning build artifacts and autosummary stubs..."
	$(AT)rm -rf "$(BUILDDIR)" $(STUBDIRS)
	$(AT)echo "✅ Clean complete."
# --------------------------------------------------
# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
# --------------------------------------------------
%: Makefile
	$(AT)echo "🏃 Running Sphinx Documentation Generator..."
	$(AT)$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	$(AT)echo "✅ Sphinx run complete."
# --------------------------------------------------
