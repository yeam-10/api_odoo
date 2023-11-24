# API Connector
# XMLRPC Style for Odoo
# Main Dev: Anyeimar Requena <erp@estrategiasdeinversion.com>
# arequena 
# -*- coding: utf-8 -*-
import logging

import odoo
from odoo import http
from odoo.http import request
import xmlrpc.client


_logger = logging.getLogger(__name__)


class ApiRest(http.Controller):


#METHOD GET
    @http.route('/ei/v1/courses', type="json", auth= 'user', method="GET")
    def get_contacts(self):

        courses_rec = request.env['slide.channel'].sudo().search([])
        _logger.info(courses_rec)
        courses = []
        for rec in courses_rec:
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
                 'user_id':rec.user_id,
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
        print('Courses lis', courses)
        data = {'status': 200, 'response': courses, 'menssge': 'Success'}
        
        return data
    
    @http.route('/ei/v1/conteiner', type="json", auth= 'user', method="GET")
    def get_conteiner(self):
        slide_rec = request.env['slide.slide'].sudo().search([])
        slides = []
        for rec in slide_rec:
            vals = {
                'name' : rec.name,
                'tag_ids': rec.tag_ids,
                #'image_1920': rec.image_1920,
                'channel_id': rec.channel_id,
                'slide_type': rec.slide_type,
                'mime_type': rec.mime_type,
                'user_id': rec.user_id,
                'completion_time': rec.completion_time,
                'is_preview': rec.is_preview,
                'slide_resource_downloadable':rec.slide_resource_downloadable,
                'date_published': rec.date_published,
                'description': rec.description,
                'link_ids': rec.link_ids,
                'slide_resource_ids': rec.slide_resource_ids,
                'quiz_first_attempt_reward': rec.quiz_first_attempt_reward,
                'quiz_second_attempt_reward': rec.quiz_second_attempt_reward,
                'quiz_third_attempt_reward': rec.quiz_third_attempt_reward,
                'quiz_fourth_attempt_reward': rec.quiz_fourth_attempt_reward,
                'question_ids': rec.question_ids,
                'slide_views': rec.slide_views,
                'public_views': rec.public_views,
                'total_views': rec.total_views,
                'channel_type':rec.channel_type,
                'channel_allow_comment': rec.channel_allow_comment,
                'likes': rec.likes,
                'dislikes':rec.dislikes,
                'comments_count': rec.comments_count,
                } 
            slides.append(vals)
        print('Conteiner list', slides)
        data = {'status': 200, 'response': slides, 'menssge': 'Success'}
        return data
    
    @http.route('/ei/v1/groups', type="json", auth= 'user', method="GET")
    def get_groups(self):
        group_rec = request.env['slide.channel.tag.group'].sudo().search([])
        groups = []
        for rec in group_rec:
            vals = {
                'name': rec.name,
                'is_published': rec.is_published,
                'tag_ids': rec.tag_ids
            }
            groups.append(vals)
        print('Groups List')
        data = {'status': 200, 'response': groups, 'menssge': 'Success'}
        return data
    

    @http.route('/ei/v1/courses', type="json", auth= 'user', method="POST")
    def post_courses(self):
        courses_cr_rec = request.env['slide.channel'].sudo().create([])
        _logger.info(courses_cr_rec)
        courses = []





         
    #@http.route('/ei/v1/clients', type="json", auth= 'user', method="GET")
    #def get_clientes(self):
    #    client_rec = request.env['slide.slide'].sudo().search([])
    #    clients= []
    #    for rec in client_rec:
    #        vals = {
    #            'channel_id': rec.channel_id,
    #            'user_id': rec.user_id,
    #            'create_date': rec.create_date,
    #            'write_date': rec.write_date,
    #            'completion':rec.completion
    #            }
    #        clients.append(vals)
    #    data  = {'status': 200, 'response': clients, 'menssge': 'Success!!'}
    #    return data


    



    




    


        



   

        

    