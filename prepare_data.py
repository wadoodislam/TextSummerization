import glob

# dataset = 'dataset/*/'
from csv import DictWriter

dataset = 'dataset/cnn/'
# dataset = 'dataset/dailymail/'

# csv_file = 'dataset/summary_target.csv'
csv_file = 'dataset/cnn/cnn_target.csv'
# csv_file = 'dataset/dailymail/dailymail_target.csv'

fields = ['filename', 'summary', 'source']


if __name__ == '__main__':
    with open(csv_file, 'w', newline='') as target_file:
        writer = DictWriter(target_file, fieldnames=fields, )
        writer.writeheader()

        for story_path in glob.glob(dataset + 'stories/*.story'):

            with open(story_path, 'r') as story:
                content = story.read().split('@highlight')
            row = {
                'filename': story_path.split('/')[-1],
                'summary': '| '.join(line.strip() for line in content[1:])
            }
            writer.writerow(row)

