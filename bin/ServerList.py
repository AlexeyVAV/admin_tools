import os
import luigi

class FetchLogTask(luigi.Task):
    def output(self):
        # return luigi.LocalTarget('my_output.log')
        # writes when something to output
        # Hive example
        partition_dict = {"year": partition_year,
                          "month": partition_month,
                          "day": partition_day}
        return luigi.hive.HivePatitionTarget(
                your_table,
                partition_dict,
                database=your_database)

    def run(self):
        # some loging that needs to be run

    def requires(self):
        # holds dependency chain
        return (DependantTask0(), DependantTask1())

class CopyFile(luigi.Task)
    def output(self):
        return luigi.LocalTarget("done_copy.log")

    def run(self):
        with self.output().open('w') as output:
            output.write("Hello\tworld")

class AggregatorTask(luigi.Task):
    def output(self):
        return luigi.LocalTask('aggregator.data')

    def run(self):
        with open('input.csv','r') as input:
            cat_count = 0
            for line in input.readlines():
                animal, age, color = line.split(',')
                    if animal == 'cat':
                        coat_count += 1

        with self.output().open('w') as out_file:
            out_file.write(cat_count)

    def requires(self):
        return [CopyFile()]

class DBExampleTask(luigi.postgres.CopyToTable):
    host = ''
    database = ''
    password = ''
    table = ''

    columns = [("date_from", "DATE"),
               ("date_to", "DATE"),
               ("cat_count", "INT")]

    def requires(self):
        return [AggregatorTask()]

#class LoadServerList


