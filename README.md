# pythonDSA

A collection of Data Structures and Algorithms implemented in Python for learning, practice, and quick reference.

## Repository layout
- `Basics/` — fundamental Python concepts, classes, and basic data structure implementations
  - `class_.py` — Python class fundamentals
  - `linked_list_class.py` — linked list class implementation
  - `linked_list_practice.py` — linked list practice exercises
  - `linkedList_dict.py` — linked list using dictionary implementation
  - `pointers_dict.py` — pointer concepts with dictionaries
  - `pointers_int.py` — pointer concepts with integers
- `Interview_Questions_LinkedList/` — linked list interview problems and solutions
  - `1_find_middle_node.py` — find middle node of linked list
  - `2_has_loop.py` — detect loop in linked list
  - `3_kth_node_from_end.py` — find kth node from end
  - `4_remove_duplicates.py` — remove duplicates from linked list
## Requirements
- Python 3.8+
- (optional) virtual environment

Quick setup:
1. python -m venv .venv
2. source .venv/bin/activate  (Windows: .venv\Scripts\activate)
3. pip install -r requirements.txt  (if present)

## Usage
Run a script directly:
- `python Basics/<script>.py` — run basic concepts and implementations
- `python Interview_Questions_LinkedList/<problem>.py` — run interview problem solutions

Examples:
- `python Basics/linked_list_class.py` — test linked list implementation
- `python Interview_Questions_LinkedList/1_find_middle_node.py` — solve middle node problem

## Contributing
- Follow PEP 8 and meaningful commit messages.
- Add tests for new algorithms or edge cases.
- Create a feature branch, open a PR, and include a short description of changes.

## Style and conventions
- Prefer type hints and docstrings for public functions/classes.
- Keep implementations self-contained and well-documented.
- Include time/space complexity notes in comments when relevant.

## License
MIT License — see LICENSE file or add one if needed.

## Contact
Open issues or PRs for improvements, bug reports, or new algorithm submissions.