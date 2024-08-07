'''from instagrapi import Client

cl = Client()
cl.login("noot_orious", "Thisisnotapassword1")
n_henriq = cl.user_id_from_username(username="n_henr1q")

#cl.direct_send(text="testing one two", user_ids=[n_henriq])

all_messages = cl.direct_threads(amount=10)

pending = cl.direct_pending_inbox()
dir_thread = cl.direct_threads(selected_filter="unread")
dir_messages = cl.direct_messages(thread_id=340282366841710301244259655543300430012)

def testing_insta(inputs):
    for input in inputs:
        print("{} \n".format(input))

print("start testing inbox")
print(pending)
testing_insta(pending)
print("finish testing inbox")
print("New Input")
#testing_insta(dir_thread)
#testing_insta(dir_messages)
print("New Input")
'''

'''
for message in messages:
    print("first pass")
    text = message.messages[0].text
    print(text)
    user_id = message.messages[0].user_id
    print(user_id)
    username = cl.user_info(user_id).username
    print(username)
'''
#organize the users by id and determine if there's a way that you don't have to keep requesting the thread information

#current idea: 

'''
[DirectThread(pk='17930956223793885', id='340282366841710301244259655543300430012', 
              messages=[DirectMessage(id='31781874280108174433670161779130368', user_id='44506526362', thread_id=340282366841710301244259655543300430012, 
                                      timestamp=datetime.datetime(2024, 8, 5, 19, 0, 57), item_type='text', is_sent_by_viewer=True, is_shh_mode=False, reactions=None, 
                                      text='testing one two', reply=None, link=None, animated_media=None, media=None, visual_media=None, media_share=None, reel_share=None, 
                                      story_share=None, felix_share=None, xma_share=None, clip=None, placeholder=None), 
                        DirectMessage(id='31780641595682228157069757448716288', user_id='3235450431', thread_id=340282366841710301244259655543300430012, 
                                      timestamp=datetime.datetime(2024, 8, 5, 0, 27, 13), item_type='text', is_sent_by_viewer=False, is_shh_mode=False, reactions=None, 
                                      text='Im gonna kick your ass you little freak', reply=None, link=None, animated_media=None, media=None, visual_media=None, media_share=None, reel_share=None, 
                                      story_share=None, felix_share=None, xma_share=None, clip=None, placeholder=None), 
                        DirectMessage(id='31780638891401445101177033203908608', user_id='44506526362', thread_id=340282366841710301244259655543300430012, 
                                    timestamp=datetime.datetime(2024, 8, 5, 0, 24, 46), item_type='text', is_sent_by_viewer=True, is_shh_mode=False, reactions=None, 
                                    text='testing one two', reply=None, link=None, animated_media=None, media=None, visual_media=None, media_share=None, reel_share=None, 
                                    story_share=None, felix_share=None, xma_share=None, clip=None, placeholder=None), 
                        DirectMessage(id='31780635936908453580421665843576832', user_id='44506526362', thread_id=340282366841710301244259655543300430012, 
                                      timestamp=datetime.datetime(2024, 8, 5, 0, 22, 6), item_type='text', is_sent_by_viewer=True, is_shh_mode=False, reactions=None, 
                                      text='testing one two', reply=None, link=None, animated_media=None, media=None, visual_media=None, media_share=None, reel_share=None, 
                                      story_share=None, felix_share=None, xma_share=None, clip=None, placeholder=None), 
                        DirectMessage(id='31767302532796562008613171589283840', user_id='44506526362', thread_id=340282366841710301244259655543300430012, 
                                      timestamp=datetime.datetime(2024, 7, 27, 15, 35, 21), item_type='text', is_sent_by_viewer=True, is_shh_mode=False, reactions=None, 
                                      text='testing one two', reply=None, link=None, animated_media=None, media=None, visual_media=None, media_share=None, reel_share=None, 
                                      story_share=None, felix_share=None, xma_share=None, clip=None, placeholder=None), 
                        DirectMessage(id='31767232984999358154426387984809984', user_id='44506526362', thread_id=340282366841710301244259655543300430012, 
                                      timestamp=datetime.datetime(2024, 7, 27, 14, 32, 30), item_type='text', is_sent_by_viewer=True, is_shh_mode=False, reactions=None, 
                                      text='testing one two', reply=None, link=None, animated_media=None, media=None, visual_media=None, media_share=None, reel_share=None, 
                                      story_share=None, felix_share=None, xma_share=None, clip=None, placeholder=None)], 
                        users=[UserShort(pk='3235450431', username='n_henr1q', full_name='Noah Henriques', 
                                         profile_pic_url=Url('https://scontent.cdninstagram.com/v/t51.2885-19/322396372_695634105617950_6883467800761665370_n.jpg?stp=dst-jpg_p206x206&_nc_cat=106&ccb=1-7&_nc_sid=fcb8ef&_nc_ohc=04pcJX7ZEFsQ7kNvgE0NhOz&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.cdninstagram.com&oh=00_AYBGQ2nIlwN8ZYmpdApNAhMQDwbg5yiAVtd7q_AFjB5L-g&oe=66B729D9'), profile_pic_url_hd=None, is_private=False)], 
                        inviter=UserShort(pk='44506526362', username='noot_orious', full_name='Noot-Noot', profile_pic_url=Url('https://instagram.fbkl1-1.fna.fbcdn.net/v/t51.2885-19/126241367_293130471960129_2090892503878761314_n.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=instagram.fbkl1-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=C7X5Wxkco_QQ7kNvgHuaIk7&edm=AI8ESKwBAAAA&ccb=7-5&oh=00_AYAwyLbZ9eZgMeazKVa1e8DrWRu4BA8sg9-P71G4qtgNrA&oe=66B7287D&_nc_sid=b1bb43'), profile_pic_url_hd=None, is_private=False), 
                        left_users=[], admin_user_ids=[], last_activity_at=datetime.datetime(2024, 8, 5, 19, 0, 57), muted=False, is_pin=None, named=False, canonical=True, pending=False, archived=False, 
                        thread_type='private', thread_title='Noah Henriques', folder=0, vc_muted=False, is_group=False, mentions_muted=False, approval_required_for_new_members=False, input_mode=0, 
                        business_thread_folder=0, read_state=0, is_close_friend_thread=False, assigned_admin_id=0, shh_mode_enabled=False, 
                        last_seen_at={'3235450431': {'timestamp': '1722832033201999', 'item_id': '31780641591234828841362826811408384', 'shh_seen_state': {}, 'created_at': '1722832032809999'}, '44506526362': {'timestamp': '1722898857007723', 'item_id': '31781874280108174433670161779130368', 'shh_seen_state': {}, 'created_at': '1722898857007723'}}), 
DirectThread(pk='18116024698377979', id='340282366841710301244259658706710115162', 
            messages=[DirectMessage(id='31780672774383247087146581457108992', user_id='10911173403', thread_id=340282366841710301244259658706710115162, 
                                    timestamp=datetime.datetime(2024, 8, 5, 0, 55, 23), item_type='text', is_sent_by_viewer=False, is_shh_mode=False, reactions=None, text='Deez mf balls bro', reply=None, link=None, animated_media=None, media=None, visual_media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, xma_share=None, clip=None, placeholder=None), DirectMessage(id='31780634958167599771454221964017664', user_id='44506526362', thread_id=340282366841710301244259658706710115162, timestamp=datetime.datetime(2024, 8, 5, 0, 21, 13), item_type='action_log', is_sent_by_viewer=True, is_shh_mode=False, reactions=None, text=None, reply=None, link=None, animated_media=None, media=None, visual_media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, xma_share=None, clip=None, placeholder=None), DirectMessage(id='31780634952520608688633959185121280', user_id='44506526362', thread_id=340282366841710301244259658706710115162, timestamp=datetime.datetime(2024, 8, 5, 0, 21, 12), item_type='text', is_sent_by_viewer=True, is_shh_mode=False, reactions=None, text='Thanks lmao', reply=None, link=None, animated_media=None, media=None, visual_media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, xma_share=None, clip=None, placeholder=None), DirectMessage(id='31780631122142487899982340036755456', user_id='10911173403', thread_id=340282366841710301244259658706710115162, timestamp=datetime.datetime(2024, 8, 5, 0, 17, 45), item_type='text', is_sent_by_viewer=False, is_shh_mode=False, reactions=None, text='Nuttiest auxabusabdieb', reply=None, link=None, animated_media=None, media=None, visual_media=None, media_share=None, reel_share=None, story_share=None, felix_share=None, xma_share=None, clip=None, placeholder=None)], users=[UserShort(pk='10911173403', username='asyaaakkuss____', full_name='Ася', profile_pic_url=Url('https://scontent.cdninstagram.com/v/t51.2885-19/451310219_1130677101568596_5339437420395273804_n.jpg?stp=dst-jpg_p206x206&_nc_cat=106&ccb=1-7&_nc_sid=fcb8ef&_nc_ohc=0eppMGVbiPYQ7kNvgGDqtg6&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.cdninstagram.com&oh=00_AYCumVDv4El-bauy07nL_-MZGqs5D9b4ED4wxDChm83fhQ&oe=66B7373F'), profile_pic_url_hd=None, is_private=True)], inviter=UserShort(pk='10911173403', username='asyaaakkuss____', full_name='Ася', profile_pic_url=Url('https://instagram.fbkl1-1.fna.fbcdn.net/v/t51.2885-19/451310219_1130677101568596_5339437420395273804_n.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=instagram.fbkl1-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=_CtabOyOozEQ7kNvgE-_QVi&edm=AI8ESKwBAAAA&ccb=7-5&oh=00_AYDKf0pd0dxBTKtdDvqRyN4KRaVfQcx-fEADACfhHQaKGA&oe=66B7373F&_nc_sid=b1bb43'), profile_pic_url_hd=None, is_private=True), left_users=[], admin_user_ids=[], last_activity_at=datetime.datetime(2024, 8, 5, 0, 55, 23), muted=False, is_pin=None, named=False, canonical=True, pending=False, archived=False, thread_type='private', thread_title='Ася', folder=0, vc_muted=False, is_group=False, mentions_muted=False, approval_required_for_new_members=False, input_mode=0, business_thread_folder=0, read_state=0, is_close_friend_thread=False, assigned_admin_id=0, shh_mode_enabled=False, last_seen_at={'10911173403': {'timestamp': '1722833719992999', 'item_id': '31780634952546784618474553038864384', 'shh_seen_state': {}, 'created_at': '1722831672925999'}, '44506526362': {'timestamp': '1722897731585999', 'item_id': '31781853519741656812683506833424384', 'shh_seen_state': {}, 'created_at': '1722897731585999'}})]
'''
l = 20
print("hi")
for index in range (l,0,-1):
    print(index)

