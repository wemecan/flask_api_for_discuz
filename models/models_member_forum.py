# coding: utf-8
from sqlalchemy import Column, Integer, SmallInteger, String, text, Text
from exts import db

class PreCommonMember(db.Model):
    __tablename__ = 'pre_common_member'

    uid = Column(Integer, primary_key=True)
    email = Column(String(40), nullable=False, server_default=text("''"))
    username = Column(String(15), nullable=False, server_default=text("''"))
    password = Column(String(32), nullable=False, server_default=text("''"))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    emailstatus = Column(Integer, nullable=False, server_default=text("'0'"))
    avatarstatus = Column(Integer, nullable=False, server_default=text("'0'"))
    videophotostatus = Column(Integer, nullable=False, server_default=text("'0'"))
    adminid = Column(Integer, nullable=False, server_default=text("'0'"))
    groupid = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    groupexpiry = Column(Integer, nullable=False, server_default=text("'0'"))
    extgroupids = Column(String(20), nullable=False, server_default=text("''"))
    regdate = Column(Integer, nullable=False, server_default=text("'0'"))
    credits = Column(Integer, nullable=False, server_default=text("'0'"))
    notifysound = Column(Integer, nullable=False, server_default=text("'0'"))
    timeoffset = Column(String(4), nullable=False, server_default=text("''"))
    newpm = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    newprompt = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    accessmasks = Column(Integer, nullable=False, server_default=text("'0'"))
    allowadmincp = Column(Integer, nullable=False, server_default=text("'0'"))
    onlyacceptfriendpm = Column(Integer, nullable=False, server_default=text("'0'"))
    conisbind = Column(Integer, nullable=False, server_default=text("'0'"))
    freeze = Column(Integer, nullable=False, server_default=text("'0'"))

class PreUcenterMember(db.Model):
    __tablename__ = 'pre_ucenter_members'

    uid = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(15), nullable=False, server_default=text("''"))
    password = Column(String(32), nullable=False, server_default=text("''"))
    email = Column(String(32), nullable=False, server_default=text("''"))
    myid = Column(String(30), nullable=False, server_default=text("''"))
    myidkey = Column(String(16), nullable=False, server_default=text("''"))
    regip = Column(String(15), nullable=False, server_default=text("''"))
    regdate = Column(Integer, nullable=False, server_default=text("'0'"))
    lastloginip = Column(Integer, nullable=False, server_default=text("'0'"))
    lastlogintime = Column(Integer, nullable=False, server_default=text("'0'"))
    salt = Column(String(6), nullable=False)
    secques = Column(String(8), nullable=False, server_default=text("''"))

class PreForumPost(db.Model):
    __tablename__ = 'pre_forum_post'

    pid = Column(Integer, nullable=False)
    fid = Column(Integer, nullable=False, server_default=text("'0'"))
    tid = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    first = Column(Integer, nullable=False, server_default=text("'0'"))
    author = Column(String(15), nullable=False, server_default=text("''"))
    authorid = Column(Integer, nullable=False, server_default=text("'0'"))
    subject = Column(String(80), nullable=False, server_default=text("''"))
    dateline = Column(Integer, nullable=False, server_default=text("'0'"))
    message = Column(String, nullable=False)
    useip = Column(String(15), nullable=False, server_default=text("''"))
    port = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    invisible = Column(Integer, nullable=False, server_default=text("'0'"))
    anonymous = Column(Integer, nullable=False, server_default=text("'0'"))
    usesig = Column(Integer, nullable=False, server_default=text("'0'"))
    htmlon = Column(Integer, nullable=False, server_default=text("'0'"))
    bbcodeoff = Column(Integer, nullable=False, server_default=text("'0'"))
    smileyoff = Column(Integer, nullable=False, server_default=text("'0'"))
    parseurloff = Column(Integer, nullable=False, server_default=text("'0'"))
    attachment = Column(Integer, nullable=False, server_default=text("'0'"))
    rate = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    ratetimes = Column(Integer, nullable=False, server_default=text("'0'"))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    tags = Column(String(255), nullable=False, server_default=text("'0'"))
    comment = Column(Integer, nullable=False, server_default=text("'0'"))
    replycredit = Column(Integer, nullable=False, server_default=text("'0'"))
    position = Column(Integer, primary_key=True, nullable=False)


class PreForumThread(db.Model):
    __tablename__ = 'pre_forum_thread'

    tid = Column(Integer, primary_key=True)
    fid = Column(Integer, nullable=False, server_default=text("'0'"))
    posttableid = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    typeid = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    sortid = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    readperm = Column(Integer, nullable=False, server_default=text("'0'"))
    price = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    author = Column(String(15), nullable=False, server_default=text("''"))
    authorid = Column(Integer, nullable=False, server_default=text("'0'"))
    subject = Column(String(80), nullable=False, server_default=text("''"))
    dateline = Column(Integer, nullable=False, server_default=text("'0'"))
    lastpost = Column(Integer, nullable=False, server_default=text("'0'"))
    lastposter = Column(String(15), nullable=False, server_default=text("''"))
    views = Column(Integer, nullable=False, server_default=text("'0'"))
    replies = Column(Integer, nullable=False, server_default=text("'0'"))
    displayorder = Column(Integer, nullable=False, server_default=text("'0'"))
    highlight = Column(Integer, nullable=False, server_default=text("'0'"))
    digest = Column(Integer, nullable=False, server_default=text("'0'"))
    rate = Column(Integer, nullable=False, server_default=text("'0'"))
    special = Column(Integer, nullable=False, server_default=text("'0'"))
    attachment = Column(Integer, nullable=False, server_default=text("'0'"))
    moderated = Column(Integer, nullable=False, server_default=text("'0'"))
    closed = Column(Integer, nullable=False, server_default=text("'0'"))
    stickreply = Column(Integer, nullable=False, server_default=text("'0'"))
    recommends = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    recommend_add = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    recommend_sub = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    heats = Column(Integer, nullable=False, server_default=text("'0'"))
    status = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    isgroup = Column(Integer, nullable=False, server_default=text("'0'"))
    favtimes = Column(Integer, nullable=False, server_default=text("'0'"))
    sharetimes = Column(Integer, nullable=False, server_default=text("'0'"))
    stamp = Column(Integer, nullable=False, server_default=text("'-1'"))
    icon = Column(Integer, nullable=False, server_default=text("'-1'"))
    pushedaid = Column(Integer, nullable=False, server_default=text("'0'"))
    cover = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    replycredit = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    relatebytag = Column(String(255), nullable=False, server_default=text("'0'"))
    maxposition = Column(Integer, nullable=False, server_default=text("'0'"))
    bgcolor = Column(String(8), nullable=False, server_default=text("''"))
    comments = Column(Integer, nullable=False, server_default=text("'0'"))
    hidden = Column(SmallInteger, nullable=False, server_default=text("'0'"))

class PreCommonMemberProfile(db.Model):
    __tablename__ = 'pre_common_member_profile'

    uid = Column(Integer, primary_key=True)
    realname = Column(String(255), nullable=False, server_default=text("''"))
    gender = Column(Integer, nullable=False, server_default=text("'0'"))
    birthyear = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    birthmonth = Column(Integer, nullable=False, server_default=text("'0'"))
    birthday = Column(Integer, nullable=False, server_default=text("'0'"))
    constellation = Column(String(255), nullable=False, server_default=text("''"))
    zodiac = Column(String(255), nullable=False, server_default=text("''"))
    telephone = Column(String(255), nullable=False, server_default=text("''"))
    mobile = Column(String(255), nullable=False, server_default=text("''"))
    idcardtype = Column(String(255), nullable=False, server_default=text("''"))
    idcard = Column(String(255), nullable=False, server_default=text("''"))
    address = Column(String(255), nullable=False, server_default=text("''"))
    zipcode = Column(String(255), nullable=False, server_default=text("''"))
    nationality = Column(String(255), nullable=False, server_default=text("''"))
    birthprovince = Column(String(255), nullable=False, server_default=text("''"))
    birthcity = Column(String(255), nullable=False, server_default=text("''"))
    birthdist = Column(String(20), nullable=False, server_default=text("''"))
    birthcommunity = Column(String(255), nullable=False, server_default=text("''"))
    resideprovince = Column(String(255), nullable=False, server_default=text("''"))
    residecity = Column(String(255), nullable=False, server_default=text("''"))
    residedist = Column(String(20), nullable=False, server_default=text("''"))
    residecommunity = Column(String(255), nullable=False, server_default=text("''"))
    residesuite = Column(String(255), nullable=False, server_default=text("''"))
    graduateschool = Column(String(255), nullable=False, server_default=text("''"))
    company = Column(String(255), nullable=False, server_default=text("''"))
    education = Column(String(255), nullable=False, server_default=text("''"))
    occupation = Column(String(255), nullable=False, server_default=text("''"))
    position = Column(String(255), nullable=False, server_default=text("''"))
    revenue = Column(String(255), nullable=False, server_default=text("''"))
    affectivestatus = Column(String(255), nullable=False, server_default=text("''"))
    lookingfor = Column(String(255), nullable=False, server_default=text("''"))
    bloodtype = Column(String(255), nullable=False, server_default=text("''"))
    height = Column(String(255), nullable=False, server_default=text("''"))
    weight = Column(String(255), nullable=False, server_default=text("''"))
    alipay = Column(String(255), nullable=False, server_default=text("''"))
    icq = Column(String(255), nullable=False, server_default=text("''"))
    qq = Column(String(255), nullable=False, server_default=text("''"))
    yahoo = Column(String(255), nullable=False, server_default=text("''"))
    msn = Column(String(255), nullable=False, server_default=text("''"))
    taobao = Column(String(255), nullable=False, server_default=text("''"))
    site = Column(String(255), nullable=False, server_default=text("''"))
    bio = Column(Text, nullable=False)
    interest = Column(Text, nullable=False)
    field1 = Column(Text, nullable=False)
    field2 = Column(Text, nullable=False)
    field3 = Column(Text, nullable=False)
    field4 = Column(Text, nullable=False)
    field5 = Column(Text, nullable=False)
    field6 = Column(Text, nullable=False)
    field7 = Column(Text, nullable=False)
    field8 = Column(Text, nullable=False)

# class PreUcenterPmIndex(db.Module):
#     __tablename__ = 'pre_ucenter_pm_indexes'
#
#     pmid = Column(Integer, primary_key=True)
#     plid = Column(Integer, nullable=False, server_default=text("'0'"))