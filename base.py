from data import *


def set_up():
    global cur, conn
    a = database()
    conn = psycopg2.connect(**a.param)
    cur = conn.cursor()
    conn.autocommit = True


def convert(fetchall):
    c = [fetchall[i][0] for i in range(len(fetchall))]
    return c


def numb(val):
    if (val == None or val == 'None'):
        return 0
    else:
        return val


def char_id(inp):
    sql = '''SELECT id FROM public.characters WHERE name='%s' '''
    cur.execute(sql % inp)
    log_i = cur.fetchall()
    log_i = convert(log_i)
    a = len(log_i)
    if a == 0:
        return None
    elif a == 1:
        return log_i[0]
    else:
        return log_i


def check_disc(did):
    sql = '''select char_id from discord where discord_id = '%s' '''
    cur.execute(sql % did)
    a = cur.fetchone()
    return a[0]


def guild_check(inp):
    sql = '''SELECT id FROM public.guilds WHERE name = '%s' '''
    cur.execute(sql % inp)
    guild_i = cur.fetchone()
    return guild_i[0]


class character:
    def __init__(self, cid):
        set_up()
        sql = '''SELECT name FROM public.characters where id = %s '''
        cur.execute(sql % cid)
        a = cur.fetchone()
        sql = '''SELECT user_id FROM public.characters where id = %s '''
        cur.execute(sql % cid)
        b = cur.fetchone()
        sql = '''SELECT weapon_type FROM public.characters where id = %s '''
        cur.execute(sql % cid)
        c = cur.fetchone()
        sql = '''SELECT hrp FROM public.characters where id = %s '''
        cur.execute(sql % cid)
        d = cur.fetchone()
        sql = '''SELECT gr FROM public.characters where id = %s '''
        cur.execute(sql % cid)
        e = cur.fetchone()
        sql = '''SELECT last_login FROM public.characters where id = %s '''
        cur.execute(sql % cid)
        f = cur.fetchone()
        sql = '''SELECT gcp FROM public.characters where id = %s '''
        cur.execute(sql % cid)
        g = cur.fetchone()
        sql = 'select gacha_prem from characters where id= %s '
        cur.execute(sql % cid)
        h = cur.fetchone()
        sql = 'select gacha_trial from characters where id= %s '
        cur.execute(sql % cid)
        i = cur.fetchone()
        sql = 'select netcafe_points from characters where id= %s '
        cur.execute(sql % cid)
        j = cur.fetchone()
        sql = 'select frontier_points from characters where id= %s '
        cur.execute(sql % cid)
        k = cur.fetchone()
        sql = 'select kouryou_point from characters where id= %s '
        cur.execute(sql % cid)
        l = cur.fetchone()
        self.cid = cid
        self.name = a[0]
        self.uid = b[0]
        self.weapon = c[0]
        self.hrp = d[0]
        self.gr = e[0]
        self.login = f[0]
        self.gcp = numb(g[0])
        self.prem = numb(h[0])
        self.trial = numb(i[0])
        self.netcafe = numb(j[0])
        self.frontier = numb(k[0])
        self.kouryou = numb(l[0])
        sql = """ select rights from users WHERE id = %s """
        cur.execute(sql % self.uid)
        m = cur.fetchone()
        sql = '''SELECT username FROM public.users where id = %s '''
        cur.execute(sql % self.uid)
        n = cur.fetchone()
        sql = '''SELECT guild_id FROM public.guild_characters WHERE character_id = %s '''
        cur.execute(sql % cid)
        o = cur.fetchone()
        if o == None:
            self.guild = 'No Guild'
            self.gid = 'No Id'
            self.gstate = 0
        else:
            sql = 'SELECT name FROM public.guilds WHERE id = %s'
            cur.execute(sql % o[0])
            p = cur.fetchone()
            self.guild = p[0]
            self.gid = o[0]
            self.gstate = 1
        self.course = m[0]
        self.username = n[0]
        try:
            sql = '''select discord_id from discord where char_id = %s '''
            cur.execute(sql % cid)
            q = cur.fetchone()
            self.discord = q[0]
            sql = 'select bounty from discord where char_id= %s '
            cur.execute(sql % cid)
            r = cur.fetchone()
            self.bounty = numb(r[0])
            sql = 'select is_male from discord where char_id= %s '
            cur.execute(sql % cid)
            s = cur.fetchone()
            if s[0] == True:
                self.gender = 'Male'
            elif s[0] == False:
                self.gender = 'Female'
        except:
            self.discord = None
            self.bounty = 0
            self.gender = 'Not Registered'

    def set_gcp(self, value):
        cid = self.cid
        sql = """ UPDATE public.characters SET gcp = %s WHERE id = %s """
        cur.execute(sql % (value, cid))

    def set_prem(self, value):
        cid = self.cid
        sql = """ UPDATE public.characters SET gacha_prem = %s WHERE id = %s """
        cur.execute(sql % (value, cid))

    def set_trial(self, value):
        cid = self.cid
        sql = """ UPDATE public.characters SET gacha_trial = %s WHERE id = %s """
        cur.execute(sql % (value, cid))

    def set_netcafe(self, value):
        cid = self.cid
        sql = """ UPDATE public.characters SET netcafe_points = %s WHERE id = %s """
        cur.execute(sql % (value, cid))

    def set_frontier(self, value):
        cid = self.cid
        sql = """ UPDATE public.characters SET frontier_points = %s WHERE id = %s """
        cur.execute(sql % (value, cid))

    def set_kouryou(self, value):
        cid = self.cid
        sql = """ UPDATE public.characters SET kouryou_point = %s WHERE id = %s """
        cur.execute(sql % (value, cid))

    def set_bounty(self, value):
        cid = self.cid
        sql = 'update discord set bounty = %s where char_id= %s '
        cur.execute(sql % (value, cid))

    def add_gcp(self, value):
        a = self.gcp+int(value)
        self.set_gcp(a)

    def add_bounty(self, value):
        a = self.bounty+int(value)
        self.set_bounty(a)

    def add_prem(self, value):
        a = self.prem+int(value)
        self.set_prem(a)

    def add_trial(self, value):
        a = self.trial+int(value)
        self.set_trial(a)

    def add_netcafe(self, value):
        a = self.netcafe+int(value)
        self.set_netcafe(a)

    def add_frontier(self, value):
        a = self.frontier+int(value)
        self.set_frontier(a)

    def add_kouryou(self, value):
        a = self.kouryou+int(value)
        self.set_kouryou(a)

    def mog(self):
        hexa = open('skin_hist.bin', 'rb').read().hex()
        sql = '''UPDATE characters SET skin_hist=(decode('%s','hex')) WHERE id= %s '''
        cur.execute(sql % (hexa, self.cid))

    def download_save(self):
        sql = '''SELECT savedata FROM characters WHERE id= %s '''
        cur.execute(sql % self.cid)
        a = cur.fetchone()
        b = open(f'{SAVE_PATH}\\savedata_{self.cid}.bin', 'wb')
        b.write(a[0])
        b.close()

    def download_partner(self):
        sql = '''SELECT partner FROM characters WHERE id= %s '''
        cur.execute(sql % self.cid)
        a = cur.fetchone()
        b = open(f'{SAVE_PATH}\\partner_{self.cid}.bin', 'wb')
        b.write(a[0])
        b.close()

    def download_file(self):
        self.download_save()
        self.download_partner()

    def boost(self):
        sql = ''' select end_time from public.login_boost_state  WHERE char_id= %s '''
        cur.execute(sql % self.cid)
        a = cur.fetchall()
        return convert(a)

    def boost_on(self):
        sql = '''UPDATE public.login_boost_state SET week_count = 5 WHERE char_id= %s'''
        sql1 = '''UPDATE public.login_boost_state SET available = true WHERE char_id= %s'''
        sql2 = ''' UPDATE public.login_boost_state SET end_time = 0 WHERE char_id= %s '''
        cur.execute(sql % self.cid)
        cur.execute(sql2 % self.cid)
        cur.execute(sql1 % self.cid)

    def boost_off(self):
        sql = ''' UPDATE public.login_boost_state SET end_time = 1 WHERE char_id= %s '''
        cur.execute(sql % self.cid)

    def guild_pkey(self):
        sql = '''SELECT id FROM public.guild_characters '''
        cur.execute(sql)
        gd_index = cur.fetchall()
        a = convert(gd_index)
        a.sort()
        return a[-1]+1

    def join_guild(self, gid):
        if self.gstate != 0:
            return
        sql = ''' INSERT INTO guild_characters (id,guild_id,character_id,joined_at,avoid_leadership,order_index) VALUES (%s,%s,%s,DEFAULT,true,DEFAULT)'''
        cur.execute(sql % (self.guild_pkey(), gid, self.cid))

    def transfer_guild(self, gid):
        b = moderator()
        a = b.guild_mem(gid)
        if self.gstate != 1:
            return
        if a >= 60:
            return
        if b.leader_id(gid) == self.cid:
            return
        sql = '''UPDATE public.guild_characters SET guild_id=%s WHERE character_id=%s '''
        cur.execute(sql % (gid, self.cid))

    def ch_rights(self, val):
        sql = """ UPDATE public.users SET rights = %s WHERE id = %s """
        cur.execute(sql % (val, self.uid))

    def unreg(self):
        sql = '''delete from discord where char_id=%s '''
        cur.execute(sql % self.cid)

    def add_data(self, did, gen):
        if gen == 'm':
            gen = 'true'
        else:
            gen = 'false'
        sql = '''insert into discord(id,char_id,discord_id,is_male) values(default,%s,'%s',%s)'''
        cur.execute(sql % (self.cid, did, gen))

    def mog(self):
        hexa = open(f'{MISC_PATH}\\skin_hist.bin', 'rb').read().hex()
        sql = '''UPDATE characters SET skin_hist=(decode('%s','hex')) where id=%s  '''
        cur.execute(sql % (hexa, self.cid))

    def upload_save(self):
        hexa = open(f'{UPLOAD_PATH}\\savedata_{self.cid}.bin',
                    'rb').read().hex()
        sql = '''UPDATE characters SET savedata=(decode('%s','hex')) WHERE id= %s '''
        cur.execute(sql % (hexa, self.cid))

    def upload_part(self):
        hexb = open(f'{UPLOAD_PATH}\\partner_{self.cid}.bin',
                    'rb').read().hex()
        sql1 = '''UPDATE characters SET partner=(decode('%s','hex')) WHERE id= %s '''
        cur.execute(sql1 % (hexb, self.cid))


class moderator:
    def leader_id(self, gid):
        sql = '''SELECT leader_id FROM public.guilds WHERE id=%s '''
        cur.execute(sql % gid)
        a = cur.fetchone()
        return a[0]

    def guild_mem(self, gid):
        sql1 = '''SELECT character_id FROM public.guild_characters WHERE guild_id = %s '''
        cur.execute(sql1 % gid)
        a = cur.fetchall()
        return len(convert(a))

    def guild_mem_id(self, gid):
        sql1 = '''SELECT character_id FROM public.guild_characters WHERE guild_id = %s '''
        cur.execute(sql1 % gid)
        a = cur.fetchall()
        return convert(a)

    def guild_name(self):
        sql = 'SELECT name FROM public.guilds order by id asc'
        cur.execute(sql)
        a = cur.fetchall()
        return convert(a)

    def guild_id(self):
        sql = 'SELECT id FROM public.guilds order by id asc'
        a = cur.execute(sql)
        guild_n = cur.fetchall()
        return convert(guild_n)

    def login_all(self):
        sql = '''SELECT last_login FROM public.characters order by last_login desc'''
        cur.execute(sql)
        a = cur.fetchall(self)
        return convert(a)

    def char_name_all(self):
        sql = '''SELECT name FROM public.characters order by last_login desc'''
        cur.execute(sql)
        id_s = cur.fetchall()
        return convert(id_s)

    def char_id_all(self):
        sql = '''SELECT id FROM public.characters order by last_login desc'''
        cur.execute(sql)
        log_i = cur.fetchall(self)
        return convert(log_i)

    def gcp_id(self):
        sql = 'SELECT id FROM public.characters WHERE gcp IS NOT NULL'
        cur.execute(sql)
        gcp_n = cur.fetchall()
        return convert(gcp_n)

    def gcp_add(self, value):
        a = self.gcp_id()
        for i in range(len(a)):
            b = character(a[i])
            b.gcp_add(value)

    def char_all(self):
        sql = 'select char_id from discord where bounty is not null order by bounty desc'
        cur.execute(sql)
        a = cur.fetchall()
        return convert(a)

    def disc_all(self):
        sql = 'select discord_id from discord where bounty is not null order by bounty desc'
        cur.execute(sql)
        a = cur.fetchall()
        return convert(a)

    def mog_all(self):
        hexa = open(f'{MISC_PATH}\\skin_hist.bin', 'rb').read().hex()
        sql = '''UPDATE characters SET skin_hist=(decode('%s','hex')) '''
        cur.execute(sql % hexa)

    def log_tof_all(self):
        sql = ''' UPDATE public.login_boost_state SET end_time = 1'''
        cur.execute(sql)

    def log_ton_all(self):
        sql = '''UPDATE public.login_boost_state SET week_count = 5 '''
        sql1 = '''UPDATE public.login_boost_state SET available = true'''
        sql2 = '''UPDATE public.login_boost_state SET end_time = 0'''
        cur.execute(sql)
        cur.execute(sql1)
        cur.execute(sql2)

# def bounty_register(self,title,solo_point,multi_point,cooldown):
##        sql = '''insert into bounty (title,solo_point,multi_point,cooldown) values ('%s',%s,%s,%s) '''
##        cur.execute(sql % (title,solo_point,multi_point,cooldown))

    def rav_trunc(self):
        sql = '''TRUNCATE TABLE raviregister RESTART IDENTITY'''
        sql1 = '''TRUNCATE TABLE ravistate RESTART IDENTITY'''
        sql2 = '''TRUNCATE TABLE ravisupport RESTART IDENTITY'''
        cur.execute(sql)
        cur.execute(sql1)
        cur.execute(sql2)

    def del_dist(self):
        sql = '''delete from distribution where bot = true '''
        cur.execute(sql)
        sql1 = '''select id from distribution where bot = true '''
        cur.execute(sql1)
        a = cur.fetchall()
        b = convert(a)
        sql2 = '''delete from distributions_accepted where distribution_id = %s '''
        for i in range(len(b)):
            cur.execute(sql2 % b[i])
