"""A video player class."""
import random

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.status = False
        self.current_video = []
        self.pause = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        videos = self._video_library.get_all_videos()
        """create list of videos"""
        video_list = []

        for i in videos:
            tags = "["
            for tag in i.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"

            video_list += [f"{i.title} ({i.video_id}) {tags}"]

        print("Here's a list of all available videos:")
        sort_list = sorted(video_list)
        for k in sort_list:
            print(k)

    def play_video(self, video_id):

        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        videos = self._video_library.get_all_videos()
        """create list of videos"""

        for i in videos:
            if i.video_id == video_id:
                if self.status:
                    print("Stopping video:", self.current_video[0])
                print("Playing video:", i.title)
                self.current_video = [i.title, i.video_id, i.tags]
                self.status = True
                return
        print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.status:
            print("Stopping video:", self.current_video[0])
            self.status = False
            return
        else:
            print("Cannot stop video. No video is currently playing.")

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_videos()
        """create list of videos"""

        random_video = random.choice(videos)

        if self.status:
            print("Stopping video:", self.current_video[0])
        print("Playing now:", random_video.title)
        self.current_video = [random_video.title, random_video.video_id, random_video.tags]
        self.status = True
        return

    def pause_video(self):
        """Pauses the current video."""
        if self.status:
            if self.pause:
                print("Video already paused:", self.current_video[0])
                return
            else:
                print("Pausing video:", self.current_video[0])
                self.pause = True
                return
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.status:
            if self.pause:
                print("Continuing video:", self.current_video[0])
                self.pause = False
                return
            else:
                print("Cannot continue video: Video is not paused")
                return
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if self.status and not self.pause:
            print("Currently playing:", self.current_video)
        elif self.status and self.pause:
            print("Currently playing:", self.current_video, "- PAUSED")
        else:
            print("No video is currently playing ")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
