"""This module is used to generate the RSS feed."""
from feedgen.feed import FeedGenerator

class Feed:
    fg = None
    """This class is used to generate the fg"""
    def generate_fg(self, feed_id, title, subtitle, link, language="en"):
        """This function is used to generate the RSS feed."""
        self.fg = FeedGenerator()
        self.fg.id(feed_id)
        self.fg.title(title)
        self.fg.subtitle(subtitle)
        self.fg.link(href=link, rel="self")
        self.fg.language(language)
        return True

    """This class is used to generate the RSS feed."""
    def generate_rss(self, fg, fe_list, file):
        """This function is used to generate the RSS feed."""
        for fe in fe_list:
            fe = fg.add_entry()
            fe.id(fe["id"])
            fe.title(fe["title"])
            fe.link(href=fe["link"], replace=True)
            fe.description(fe["description"])
            fe.pubDate(fe["pubDate"])
        fg.rss_str(pretty=True)
        fg.rss_file(file)
        return True
