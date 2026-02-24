# Makefile
# =========================================
# Project: github-docs for homelab
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
# ⚙️ Build Settings
# --------------------------------------------------
PACKAGE_NAME = "homelab"
AUTHOR = "Jared Cook"
VERSION = "1.0.0"
PUBLISHDIR ?=
# --------------------------------------------------
# 📚 Documentation (Sphinx + Jekyll)
# --------------------------------------------------
RUBY_INSTALL := bundle install
JEKYLL_BUILD := bundle exec jekyll build --trace --verbose
JEKYLL_CLEAN := bundle exec jekyll clean
JEKYLL_SERVE := bundle exec jekyll serve
# --------------------------------------------------
.PHONY: all ruby-install jekyll jekyll-serve build run clean help
# --------------------------------------------------
# Default:
# --------------------------------------------------
all: ruby-install build
# --------------------------------------------------
# ♦️ Ruby
# --------------------------------------------------
ruby-install:
	$(AT)$(RUBY_INSTALL)
# --------------------------------------------------
# 📚 Documentation (Jekyll)
# --------------------------------------------------
jekyll:
	$(AT)echo "🔨 Building Jekyll site 📚..."
	$(AT)$(JEKYLL_BUILD)
	$(AT)echo "✅ Full documentation build complete!"

jekyll-serve:
	$(AT)echo "🚀 Starting Jekyll development server..."
	$(AT)$(JEKYLL_SERVE)

build: jekyll
run: jekyll-serve
# --------------------------------------------------
# 🧹 Clean artifacts
# --------------------------------------------------
clean:
	$(AT)echo "🧹 Cleaning Jekyll build artifacts..."
	$(AT)$(call run_ci_safe,$(JEKYLL_CLEAN))
	$(AT)echo "✅ Cleaned Jekyll build artifacts."
# --------------------------------------------------
# Help
# --------------------------------------------------
help:
	$(AT)echo "📦 $(PACKAGE_NAME) github documentation Makefile"
	$(AT)echo "   author: $(PACKAGE_AUTHOR)"
	$(AT)echo "   version: $(PACKAGE_VERSION)"
	$(AT)echo ""
	$(AT)echo "Usage:"
	$(AT)echo "  make ruby-install           Installs Gemfile packages."
	$(AT)echo "  make build                  Generate Jekyll documentation"
	$(AT)echo "  make run                    Serve Jekyll site locally"
	$(AT)echo "  make clean                  Clean Jekyll build artifacts"
	$(AT)echo "  make all                    Run make (build)"
	$(AT)echo "Options:"
	$(AT)echo "  V=1             Enable verbose output (show all commands being executed)"
	$(AT)echo "  make -s         Run completely silently (suppress make's own output AND command echo)"
