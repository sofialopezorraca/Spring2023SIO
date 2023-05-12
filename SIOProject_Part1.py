# Import
import pandas as pd


# Functions
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
    df = read_file("CAZy_annotation_list.csv")

    # remove middle column of data frame
    df2 = []
    for row in df:
        df2.append((row[0], row[2]))
    df = df2
    print(df[0:5])

    # create new set with no duplicates
    df_no_duplicates = list(set(df))

    # create a new list of just the first index (the annotation) of each column
    annotation_list = []
    for row in df_no_duplicates:
        annotation_list.append(row[1])

    annotation_list_no_duplicates = list(set(annotation_list))

    # create a new list counting the amount of times an annotation occurs
    count_per_annotation = []
    for annotation in annotation_list_no_duplicates:
        count = annotation_list.count(annotation)
        count_per_annotation.append((annotation, count))

    # merge the upper two lists into one list using zip() function
    annotation_and_count_list = count_per_annotation  # [(annotation,count) for annotation,count in zip(annotation_list, count_per_annotation)]

    # remove any repetitions from the final list
    final_list = []
    for row in annotation_and_count_list:
        if row not in final_list:
            final_list.append(row)

    # convert final_list into a data frame
    col_names = ['Annotation', 'Count']
    final_df = pd.DataFrame(final_list, columns=col_names)
    final_df = final_df.sort_values(by='Count', ascending=True)
    print(final_df)
    final_df.to_csv("count_annotation.csv", header=True, index=False, sep=",")
