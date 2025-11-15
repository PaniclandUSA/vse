# Contributing to VSE

Thank you for your interest in contributing to **Vector-Space Esperanto (VSE)**! This project represents a collaborative effort to build the first universal semantic control protocol for AI systems.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear, descriptive title
- Steps to reproduce the problem
- Expected vs. actual behavior
- Your environment (Python version, OS)
- Relevant code samples or VSE packets

### Suggesting Features

We welcome feature suggestions! Please open an issue with:
- A clear description of the feature
- Use cases and benefits
- How it fits into VSE's architecture (v1.3, Kinetic, or Gregarious)
- Example VSE packets demonstrating the feature

### Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/stonespell72/vse.git
   cd vse
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set up development environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

4. **Make your changes**
   - Follow the coding standards (see below)
   - Add tests for new functionality
   - Update documentation as needed

5. **Run tests**
   ```bash
   pytest tests/ -v
   black vse_core vse_metrics tests examples
   flake8 vse_core vse_metrics
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```

7. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Coding Standards

### Python Style
- Follow **PEP 8** guidelines
- Use **Black** for formatting (line length: 100)
- Use **type hints** where appropriate
- Write **docstrings** for all public functions/classes

### Documentation
- Update README.md if adding user-facing features
- Add docstrings following Google style
- Update examples/ if needed
- Keep docs/ synchronized with code changes

### Testing
- Maintain >80% code coverage
- Write unit tests for all new functions
- Add integration tests for complex features
- Test edge cases and error conditions

### Commit Messages
Use clear, descriptive commit messages:
```
Add GSN network handshake protocol

- Implement UUID-based node registration
- Add curiosity spillover algorithm
- Update URP stabilization logic
```

## Project Structure

```
vse/
├── vse_core/          # Core packet handling
├── vse_metrics/       # Metric computation
├── vse_kinetic/       # v1.4 Kinetic (Gemini)
├── vse_gregarious/    # v1.4 Gregarious (Grok)
├── tests/             # Test suite
├── examples/          # Usage examples
├── docs/              # Documentation
└── notebooks/         # Jupyter tutorials
```

## Areas Needing Contribution

### High Priority
- [ ] Complete vse_kinetic/ module implementation
- [ ] Complete vse_gregarious/ module implementation
- [ ] Visualization tools (GSN topology viewer)
- [ ] VS Code extension for .vse files
- [ ] Jupyter notebook tutorials

### Medium Priority
- [ ] CLI tools (vse-validate, vse-migrate)
- [ ] Metric computation optimizations
- [ ] Additional examples for different domains
- [ ] Performance benchmarks

### Documentation
- [ ] API reference completion
- [ ] Architecture deep-dive guide
- [ ] Tutorial notebooks
- [ ] Best practices guide

## VSE Architecture Layers

When contributing, understand the three layers:

### v1.3 (Stable)
- Core syntax: intent, constraints, divergence, immune
- Validation and parsing
- JSON/VSE serialization

### v1.4 Kinetic (Gemini AI)
- KBM: Kinetic Boundary Management
- C-TVM: Contextual Token-Vector Mapping
- μ-Loop: Real-time monitoring
- Foundation: Semantic anchors

### v1.4 Gregarious (Grok/xAI)
- GSN: Gregarious Semantic Networks
- EVF: Exploratory Vector Fields
- URP: Universal Resonance Protocol
- Network-scale coordination

## Code Review Process

All contributions go through code review:
1. Automated CI/CD checks must pass
2. At least one maintainer approval required
3. Code coverage must not decrease
4. Documentation must be updated

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help newcomers
- Credit others' work appropriately

## Questions?

- Open an issue for questions
- Join discussions in GitHub Discussions
- Email: john@example.com (placeholder)

---

**Thank you for contributing to VSE!**

*Control the vector. Shape the future.*
