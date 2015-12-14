import sys
import csv
import re

def mapper():
# read standard input line by line
     reader = csv.reader(sys.stdin, delimiter='\t')

     for line in reader:
          print line
          for w in line:
               data = re.split("[/. ,;!?:\"()<>#$=-]+",w)
               for s in data:
                    # keyword - ID
                    print "{0}\t{1}".format(s.lower(), line[0])


#"id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	"state_string"	"last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"	"extra"	"extra_ref_id"	"extra_count"	"marked"

test_text = """5339\tWhether pdf of Unit and Homework is available?\tcs101 pdf\t100000458\tBody\tquestion\t\\n\t\\n\t2012-02-25 08:09:06.787181+00\t1\t\t\\n\t100000921\t2012-02-25 08:11:01.623548+00\t6922\t\\n\t\\n\t204\tf
2312\tFeedback on Audio Quality\tcs101 production audio\t100005361\t<p>We are looking for feedback on the audio in our videos. Tell us what you think and try to be as <em>specific</em> as possible.</p>\tquestion\t\\n\t\\n\t2012-02-23 00:28:02.321344+00\t2\t\t\\n\t201398145\t2014-01-14 17:18:35.613939+00\t2960\t\\n\t\\n\t524\tf
"""

# See 'MapReduce Design Patterns' page 50
def main():
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)
	mapper()
	sys.stdin = sys.__stdin__

main()
