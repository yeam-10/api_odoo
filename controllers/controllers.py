# API Connector
# XMLRPC Style for Odoo
# Main Dev: Anyeimar Requena <ierp@estrategiasdeinversion.com>
# arequena 
# -*- coding: utf-8 -*-
import logging

import odoo
from odoo import http
from odoo.http import request


_logger = logging.getLogger(__name__)


class ApiRest(http.Controller):

    @http.route('/ei/v1/courses', type="json", auth= 'user', method="GET")
    def get_contacts(self):

        courses_rec = request.env['slide.channel'].sudo().search([])
        _logger.info(courses_rec)
        courses = []
        for rec in courses_rec:
         courses = []
         for item in rec:
            vals = {
            'id' : rec.id,
            'name': rec.name,
            #'image_1920': rec.image_1920,
            'members_count':rec.members_count,
            'total_views':rec.total_views,
            'total_slides': rec.total_slides,
            'members_done_count': rec.members_done_count,
            'rating_avg_stars': rec.rating_avg_stars,
            'rating_count': rec.rating_count,
            'is_published': rec.is_published,
            'slide_ids':rec.slide_ids,
            'description': rec.description,
            'user_id':item.user_id,
            #'forum_id': rec.forum_id, Este campo debe descomentarse en produccion
            'publish_template_id': rec.publish_template_id,
            'share_template_id': rec.share_template_id,
            'completed_template_id': rec.completed_template_id,
            'enroll': rec.enroll,
            'upload_group_ids': rec.upload_group_ids,
            'channel_type': rec.channel_type,
            'visibility':rec.visibility,
            'promoted_strategy': rec.promote_strategy,
            'promoted_slide_id': rec.promoted_slide_id,
            'tag_ids': rec.tag_ids,
            'karma_gen_channel_rank':rec.karma_gen_channel_rank,
            'karma_gen_channel_finish':rec.karma_gen_channel_finish,
            'karma_review': rec.karma_review,
            'karma_slide_comment': rec.karma_slide_comment,
            'karma_slide_vote': rec.karma_slide_vote,

        }
            courses.append(vals)
        print('Contacs lis', courses)
        data = {'status': 200, 'response': courses, 'menssge': 'Success'}
        
        return data
        
    #@http.route('ei/v1/courses/count', type="json", auth= 'user', method="GET")
    #def get_courses_search(self):
    #    ourses_search = request.env['slide.channel'].sudo().search([])
    #    courses = []


   

        

    