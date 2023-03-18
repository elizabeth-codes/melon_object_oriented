############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self,
        name,
        code,
        first_harvest,
        color,
        is_seedless,
        is_bestseller,
    ):
        """Initialize a melon."""

        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

    # def repr(self):
    #     return f"<melon name = {self.name}>"
    """Question for Meggin: 
    When will we have to call this definition in order to use it with other methods/functions?"""


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    #cat = Cat()
    muskmelon = MelonType("muskmelon", "musk", 1998, "green", True, True)
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)
    casaba = MelonType("Casaba", "cas", 2003, "orange", True, False)
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)
    crenshaw = MelonType("Crenshaw", "cren", 1996, "green", True, False)
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)
    yellow_watermelon = MelonType("Yellow Watermelon", "yw", 2013, "yellow",
                                  True, True)
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    # print(all_melon_types)
    return all_melon_types


melon_types = make_melon_types()
# print(melon_types)
# # loop through and print the pairing of each one
for items in melon_types:

    print(f"{items.pairings} {items.name}")


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for items in melon_types:
        pairing_string = ",".join(items.pairings)
        print(f"{items.name} pairs with ")
        print(f"- {pairing_string}")


print_pairing_info(melon_types)
# Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dict = {}
    for item in melon_types:
        # print(item)
        melon_dict[item.code] = item

    return melon_dict


print(make_melon_type_lookup(melon_types))

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(
        self,
        melon_type,
        shape_rating,
        color_rating,
        harvested_from_field,
        harvested_by,
    ):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from_field = harvested_from_field
        self.harvested_by = harvested_by


#Creating a method called issellable#

    def is_sellable(self):
        if self.harvested_from_field != 3 and self.shape_rating > 5 and self.shape_rating > 5:
            return True

        return False


def make_melons(melon_types):
    melon_dict = make_melon_type_lookup(melon_types)
    """Returns a list of Melon objects."""
    Melon1 = Melon(melon_dict["yw"], 8, 7, 2, "sheila")
    Melon2 = Melon(melon_dict["yw"], 3, 4, 2, "sheila")
    Melon3 = Melon(melon_dict["yw"], 9, 8, 3, "sheila")
    Melon4 = Melon(melon_dict["cas"], 10, 6, 35, "sheila")
    Melon5 = Melon(melon_dict["cren"], 8, 9, 35, "Michael")
    Melon6 = Melon(melon_dict["cren"], 8, 2, 35, "Michael")
    Melon7 = Melon(melon_dict["cren"], 2, 3, 4, "Michael")
    Melon8 = Melon(melon_dict["musk"], 6, 7, 4, "Michael")
    Melon9 = Melon(melon_dict["yw"], 7, 10, 3, "sheila")

    # Fill in the rest
    melon_list = [
        Melon1, Melon2, Melon3, Melon4, Melon5, Melon6, Melon7, Melon8, Melon9
    ]

    return melon_list


melon_list = make_melons(melon_types)
# print(make_melons(melon_types))


def get_sellability_report(melon_list):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melon_list:
        sellable_or_not = ""
        if melon.is_sellable() is True:
            sellable_or_not = "Can be sold"
            print(
                f"Harvested by {melon.harvested_by} from Field {melon.harvested_from_field} {sellable_or_not}"
            )
        else:
            sellable_or_not = "Not sellable"
            print(
                f"Harvested by {melon.harvested_by} from Field {melon.harvested_from_field} {sellable_or_not}"
            )


print(get_sellability_report(melon_list))

# for reference
# for items in melon_types:
#         pairing_string = ",".join(items.pairings)
#         print(f"{items.name} pairs with ")
#         print(f"- {pairing_string}")