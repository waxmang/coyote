from django import forms

class IngredientForm(forms.Form):
    CHOICES = (
        ("egg", "Egg"),
        ("milk", "Milk"),
        ("cheese", "Cheese"),
        ("bread", "Bread"),
        ("bacon", "Bacon"),
        ("bagel", "Bagel"),
        ('apple', 'Apple'),
        ('pear', 'Pear'),
        ('banana', 'Banana'),
        ('lemon', 'Lemon'),
        ('lime', 'Lime'),
        ('orange', 'Orange'),
        ('avocado', 'Avocado'),
        ('carrot', 'Carrot'),
        ('lettuce', 'Lettuce'),
        ('cabbage', 'Cabbage'),
        ('eggplant', 'Eggplant'),
        ('potato', 'Potato'),
        ('taro', 'Taro'),
        ('tomato', 'Tomato'),
        ('celery', 'Celery'),
        ('kale', 'Kale'),
        ('onion', 'Onion'),
        ('garlic', 'Garlic'),
        ('radish', 'Radish'),
        ('spinach', 'Spinach'),
        ('chard', 'Chard'),
        ('broccoli', 'Broccoli'),
        ('cauliflower', 'Cauliflower'),
        ('corn', 'Corn'),
        ('beet', 'Beet'),
        ('cucumber', 'Cucumber'),
        ('bean', 'Bean'),
        ('okra', 'Okra'),
        ('pumpkin', 'Pumpkin'),
        ('arugula', 'Arugula'),
        ('papaya', 'Papaya'),
        ('olive', 'Olive'),
        ('zucchini', 'Zucchini'),
        ('pumpkin', 'Pumpkin'),
        ('squash', 'Squash'),
        ('tofu', 'Tofu'),
        ('ham', 'Ham'),
        ('ribeye', 'Ribeye'),
        ('beef-ribs', 'Beef Ribs'),
        ('ground-beef', 'Ground Beef'),
        ('cow-tongue', 'Cow Tongue'),
        ('new-york-strip', 'New York Strip'),
        ('chicken-breast', 'Chicken Breast'),
        ('chicken-thigh', 'Chicken Thigh'),
        ('chicken-drumsticks', 'Chicken Drumsticks'),
        ('pork', 'Pork'),
        ('duck', 'Duck'),
        ('lamb', 'Lamb'),
        ('salmon', 'Salmon'),
        ('tuna', 'Tuna'),
        ('trout', 'Trout'),
        ('catfish', 'Catfish'),
        ('squid', 'Squid'),
        ('eel', 'Eel'),
        ('octopus', 'Octopus'),
        ('lobster', 'Lobster'),
        ('crab', 'Crab'),
        ('shrimp', 'Shrimp'),
        ('crawfish', 'Crawfish'),
        ('salt', 'Salt'),
        ('pepper', 'Pepper'),
        ('sugar', 'Sugar'),
        ('mayonnaise', 'Mayonnaise'),
        ('cayenne', 'Cayenne'),
        ('paprika', 'Paprika'),
        ('cumin', 'Cumin'),
        ('vegetable-oil', 'Vegetable Oil'),
        ('vinegar', 'Vinegar'),
        ('vanilla', 'Vanilla'),
        ('tomato-sauce', 'Tomato Sauce'),
        ('pasta', 'Pasta'),
        ('yeast', 'Yeast'),
        ('flour', 'Flour'),
        ('chocolate', 'Chocolate'),
        ('nuts', 'Nuts'),
        ('oatmeal', 'Oatmeal'),
        ('ginger', 'Ginger'),
        ('thyme', 'Thyme'),
        ('rosemary', 'Rosemary'),
        ('dill', 'Dill'),
        ('cayenne', 'Cayenne'),
    )

    picked = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
