# We make the dataset isolated and clean by making it this way


class Dataset:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]


dataset = [
    {"text": "Limited time offer click now", "label": "SPAM"},
    {"text": "Meeting at 2 PM with the manager", "label": "HAM"},
    {
        "text": "You win! Claim your prize by submitting your bank account",
        "label": "SPAM",
    },
    {"text": "Project discussion tomorrow at 10 AM", "label": "HAM"},
    # Spams
    {"text": "Exclusive offer just for you", "label": "SPAM"},
    {"text": "Don't miss this! Claim your prize now", "label": "SPAM"},
    {"text": "Click here to win prize", "label": "SPAM"},
    # Not Spams (Hams)
    {"text": "Meeting at 2 PM with manager", "label": "HAM"},
    {"text": "Project discussion tomorrow", "label": "HAM"},
    {"text": "Team meeting schedule confirmed", "label": "HAM"},
]

dataset = Dataset(dataset)
