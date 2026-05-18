# Package initializer
# Personal fork: added version tracking for local dev reference
__version__ = "0.1.0-local"
__author_fork__ = "personal learning fork"
__all__ = []

# Note: bumping version to track my local changes more easily
# See CHANGELOG.md (if I ever write one) for what I've changed
__fork_notes__ = "experimenting with agent routing logic"

# Quick sanity check - useful when importing in notebooks or scripts
if __name__ == "__init__":
    print(f"[fork] openai-cs-agents-demo v{__version__} loaded")
