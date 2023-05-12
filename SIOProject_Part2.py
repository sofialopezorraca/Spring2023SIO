# Import
from collections import defaultdict
from collections import Counter
import pandas as pd


# turn data in file into data frame using pandas
def read_file(filename):
    '''
    Take annotation data from an outside program written in a tab-delimited format.
    :param filename: This is the file that I want to read in
    :return: I will return a table representing the file that I read in. This table will have 3 columns, "genome", "gene", and "annotation".
    '''
    df = pd.read_csv(filename, sep=",")
    df = df.values.tolist()
    return df


if __name__ == '__main__':
    '''
    This is your main function area. 
    This is the code that will be run when running this script from the command line.
    '''
    # call read_file()
    list1 = read_file("CAZy_annotation_list.csv")

    # create dictionary from the list, keeping all values for each key + deleting middle row
    dictionary = defaultdict(list)
    for row in list1:
        dictionary[row[0]].append(row[2])

    # create a list with only the value pairs
    value_list = list(dictionary.values())
    print("done parse")

    # create new list of cartesian products of the values inside each row of value_list
    i = 0
    cartesian_value_list = []
    set_for_inner_list = set()
    for inner_list in value_list:
        for i in range(0, len(inner_list)):
            for j in range(i + 1, len(inner_list)):
                set_for_inner_list.add((inner_list[i], inner_list[j]))

        for item in set_for_inner_list:
            cartesian_value_list.append(item)
        set_for_inner_list = set()
    print("done pairing")

    # count the amount of times each pair of annotations happens
    # cartesian_value_list_count = []
    # for pair in cartesian_value_list:
    #    annotation_pair_repetition = cartesian_value_list.count(pair)
    #    cartesian_value_list_count.append(annotation_pair_repetition)
    print("done counting")

    # final_dictionary = dict(zip(cartesian_value_list, cartesian_value_list_count))
    print("done zipping")

    final_dictionary = Counter(cartesian_value_list)

    list_of_lists = [[a, b, count] for (a, b), count in final_dictionary.items()]
    df = pd.DataFrame(list_of_lists, columns=["PairA", "PairB", "count"]).sort_values(by=["count"])
    print(df)
