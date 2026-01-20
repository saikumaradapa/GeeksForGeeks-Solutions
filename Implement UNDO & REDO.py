class Solution:
    def __init__(self):
        self.doc = []          # current document
        self.undo_stack = []   # history of appends
        self.redo_stack = []   # history of undone operations

    def append(self, x):
        # Append character to document
        self.doc.append(x)
        self.undo_stack.append(x)
        self.redo_stack.clear()

    def undo(self):
        # Undo last append
        if self.undo_stack:
            ch = self.undo_stack.pop()
            self.doc.pop()
            self.redo_stack.append(ch)

    def redo(self):
        # Redo last undone append
        if self.redo_stack:
            ch = self.redo_stack.pop()
            self.doc.append(ch)
            self.undo_stack.append(ch)

    def read(self):
        # Return document content
        return "".join(self.doc)
