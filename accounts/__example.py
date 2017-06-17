# -*- coding:utf-8 -*-

CONFIG = dict(
    login="",
    password="",
    like_per_day=100,
    comments_per_day=10,
    tag_list=['f4f', 'l4l', 'follow4follow', 'like4like'],
    tag_blacklist=['rain', 'thunderstorm'],
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=0,
    follow_time=1 * 60,
    unfollow_per_day=0,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=1,
    proxy='',
    media_max_like=5,
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["this", "the", "your"],
                  ["photo", "picture", "pic", "shot", "snapshot"],
                  ["is", "looks", "feels", "is really"],
                  ["great", "super", "good", "very good", "good", "wow",
                   "WOW", "cool", "GREAT","magnificent", "magical",
                   "very cool", "stylish", "beautiful", "so beautiful",
                   "so stylish", "so professional", "lovely",
                   "so lovely", "very lovely", "glorious","so glorious",
                   "very glorious", "adorable", "excellent", "amazing"],
                  [".", "..", "...", "!", "!!", "!!!"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=['example_user_1', 'example_user_2']
)
