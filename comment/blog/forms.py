#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fluent_comments.forms import CompactLabelsCommentForm


class CommentForm(CompactLabelsCommentForm):
    """
    The comment form to use
    """
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['url'].label = "blog"
