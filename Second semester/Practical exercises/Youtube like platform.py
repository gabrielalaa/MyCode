import random
import datetime

class Video:
    def __init__(self, title, description, duration, upload_date):
        self.title = title
        self.description = description
        self.duration = duration
        self.upload_date = upload_date

        self.views = 0
        self.likes = 0
        self.dislikes = 0
        self.comments = []

        self.video_id = random.randint(1, 1000)

    def view(self):
        self.views += 1

    def like(self):
        self.likes += 1

    def dislike(self):
        self.dislikes += 1

    def __repr__(self):
        return (f"Video: {self.title}\nDescription: {self.description}\n"
                f"Duration: {self.duration} seconds\nViews: {self.views}\n"
                f"Likes: {self.likes}\nDislikes: {self.dislikes}\n"
                f"Upload Date: {self.upload_date}\nVideo ID: {self.video_id}")


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        self.uploaded_videos = []
        self.history = []
        self.comments = []
        self.subscriptions = []  # New attribute to store subscriptions

        self.channel = None

    def upload_video(self, video):
        self.uploaded_videos.append(video)
        print(f"{self.name} uploaded a new video: '{video.title}'")

    def watch_video(self, video):
        self.history.append(video)
        video.view()
        feedback = input("Do you like the video? (y/n): ").lower()
        if feedback == "y":
            video.like()
        elif feedback == "n":
            video.dislike()
        else:
            print("You didn't like or dislike the video")

    def create_channel(self, channel_name):
        self.channel = Channel(channel_name, self)
        for video in self.uploaded_videos:
            self.channel.add_video(video)
        print(f"Channel '{channel_name}' created for {self.name}.")

    def comment(self, text, video):
        comment = Comment(text, self)
        video.comments.append(comment)
        self.comments.append(comment)
        print(f"{self.name} commented on '{video.title}': {text}")

    def subscribe(self, channel):
        if channel not in self.subscriptions:
            self.subscriptions.append(channel)
            channel.subscribers.append(self)
            print(f"{self.name} subscribed to '{channel.channel_name}'")
        else:
            print(f"{self.name} is already subscribed to '{channel.channel_name}'")

    def unsubscribe(self, channel):
        if channel in self.subscriptions:
            self.subscriptions.remove(channel)
            channel.subscribers.remove(self)
            print(f"{self.name} unsubscribed from '{channel.channel_name}'")
        else:
            print(f"{self.name} is not subscribed to '{channel.channel_name}'")

    def __repr__(self):
        return (f"User: {self.name} ({self.email})\n"
                f"Uploaded Videos: {len(self.uploaded_videos)}\n"
                f"Watched Videos: {len(self.history)}")


class Channel:
    def __init__(self, channel_name, owner):
        self.channel_name = channel_name
        self.owner = owner  # Now `owner` is a User object
        self.videos = []
        self.subscribers = []  # New attribute to store subscribers

    def add_video(self, video):
        self.videos.append(video)
        print(f"Video '{video.title}' added to channel '{self.channel_name}'.")

        # Notify subscribers about the new video
        for subscriber in self.subscribers:
            print(f"Notification: {subscriber.name}, a new video '{video.title}' has been uploaded to '{self.channel_name}'!")

    def get_video(self, video_id):
        for video in self.videos:
            if video.video_id == video_id:
                return video
        return None

    def __repr__(self):
        return (f"Channel: {self.channel_name}\n"
                f"Owner: {self.owner.name}\n"
                f"Total Videos: {len(self.videos)}")


class Comment:
    def __init__(self, text, user):
        self.text = text
        self.user = user
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def edit_comment(self, new_text):
        self.text = new_text
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Comment updated.")

    def __repr__(self):
        return f"User: {self.user.name}\nComment: {self.text}\nDate: {self.date}"


# Testing the Video, User, Channel, and Subscription functionality
v1 = Video("Introduction to Python", "A beginner's guide to Python.", 600, "2024-09-05")
v1.view()
v1.like()
v1.dislike()
print(v1)
print('\n')

user1 = User('Sabina', 'sabina@gmail.com')
user1.upload_video(Video('Cookies', 'Watch me making cookies.', 200, '2024-09-05'))
print(user1.uploaded_videos)
user1.watch_video(v1)
print(v1)

user1.create_channel('Cook with Sabina')

channel = user1.channel
if channel:
    video_id = v1.video_id
    retrieved_video = channel.get_video(video_id)
    if retrieved_video:
        print(f"Video found: {retrieved_video.title} (ID: {retrieved_video.video_id})")
    else:
        print("Video not found.")

# User comments on a video
user1.comment('Nice video!', v1)

# Display and possibly edit the comments
for comment in user1.comments:
    print(comment)
    answer = input("Do you want to change the comment (y/n): ").lower()
    if answer == "y":
        new_comment = input(f"Change the comment: {comment.text}: ")
        comment.edit_comment(new_comment)
        print(comment)

# User subscribes to a channel
user2 = User('Alex', 'alex@gmail.com')
user2.subscribe(channel)

# Adding a new video to notify subscribers
new_video = Video("Chocolate Cake", "Learn to bake a chocolate cake.", 300, "2024-09-10")
channel.add_video(new_video)

# User unsubscribes from a channel
user2.unsubscribe(channel)