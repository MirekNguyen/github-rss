"""This module is used to generate the RSS feed."""
from feedgen.feed import FeedGenerator

class Feed:
    """This class is used to generate the RSS feed."""
    fg = FeedGenerator()
    """Generate fg as wrapper"""
    def generate_fg(self, feed_id, title, subtitle, link, language="en") -> bool:
        """This function is used to generate the RSS feed."""
        self.fg.id(feed_id)
        self.fg.title(title)
        self.fg.subtitle(subtitle)
        self.fg.link(href=link, rel="self")
        self.fg.language(language)
        return True

    """This method is used to generate the RSS feed."""
    def generate_rss(self, fe_list, file) -> bool:
        """This function is used to generate the RSS feed."""
        for feed in fe_list:
            fe = self.fg.add_entry()
            fe.id(feed["id"])
            fe.title(feed["title"])
            fe.link(href=feed["link"], replace=True)
            fe.description(feed["description"])
            fe.pubDate(feed["pubDate"])
        self.fg.rss_str(pretty=True)
        self.fg.rss_file(file)
        return True
