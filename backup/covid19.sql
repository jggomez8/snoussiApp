PGDMP     +                    x            covid19    9.6.17    9.6.17 �    o	           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            p	           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            q	           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            r	           1262    37501    covid19    DATABASE     �   CREATE DATABASE covid19 WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Spain.1252' LC_CTYPE = 'Spanish_Spain.1252';
    DROP DATABASE covid19;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            s	           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12387    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            t	           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    37533 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         postgres    false    3            �            1259    37531    auth_group_id_seq    SEQUENCE     z   CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       postgres    false    192    3            u	           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
            public       postgres    false    191            �            1259    37543    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         postgres    false    3            �            1259    37541    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       postgres    false    3    194            v	           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
            public       postgres    false    193            �            1259    37525    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         postgres    false    3            �            1259    37523    auth_permission_id_seq    SEQUENCE        CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       postgres    false    3    190            w	           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
            public       postgres    false    189            �            1259    37640    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         postgres    false    3            �            1259    37638    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       postgres    false    3    202            x	           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
            public       postgres    false    201            �            1259    37515    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         postgres    false    3            �            1259    37513    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       postgres    false    3    188            y	           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
            public       postgres    false    187            �            1259    37504    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         postgres    false    3            �            1259    37502    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public       postgres    false    186    3            z	           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
            public       postgres    false    185            �            1259    37828    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         postgres    false    3            �            1259    37664    rrhh_biometric    TABLE     �  CREATE TABLE public.rrhh_biometric (
    id integer NOT NULL,
    date_joined date NOT NULL,
    date_joinedtime timestamp with time zone NOT NULL,
    hour time without time zone NOT NULL,
    "hourEntradaM" time without time zone,
    "hourSalidaM" time without time zone,
    "hourEntradaV" time without time zone,
    "hourSalidaV" time without time zone,
    "hourExtra" integer NOT NULL,
    emp_id integer NOT NULL
);
 "   DROP TABLE public.rrhh_biometric;
       public         postgres    false    3            �            1259    37662    rrhh_biometric_id_seq    SEQUENCE     ~   CREATE SEQUENCE public.rrhh_biometric_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.rrhh_biometric_id_seq;
       public       postgres    false    204    3            {	           0    0    rrhh_biometric_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.rrhh_biometric_id_seq OWNED BY public.rrhh_biometric.id;
            public       postgres    false    203            �            1259    37672    rrhh_employee    TABLE       CREATE TABLE public.rrhh_employee (
    id integer NOT NULL,
    dependence character varying(50) NOT NULL,
    birthdate date NOT NULL,
    cant_familiar integer NOT NULL,
    gender character varying(20) NOT NULL,
    state boolean NOT NULL,
    user_id integer NOT NULL
);
 !   DROP TABLE public.rrhh_employee;
       public         postgres    false    3            �            1259    37670    rrhh_employee_id_seq    SEQUENCE     }   CREATE SEQUENCE public.rrhh_employee_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.rrhh_employee_id_seq;
       public       postgres    false    3    206            |	           0    0    rrhh_employee_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.rrhh_employee_id_seq OWNED BY public.rrhh_employee.id;
            public       postgres    false    205            �            1259    37680    rrhh_symptomsemp    TABLE     �  CREATE TABLE public.rrhh_symptomsemp (
    id integer NOT NULL,
    date_joined date NOT NULL,
    body_temperature integer NOT NULL,
    air_death integer NOT NULL,
    dry_cough integer NOT NULL,
    intestinal_discomfort integer NOT NULL,
    headache integer NOT NULL,
    lost_taste integer NOT NULL,
    lost_olfato integer NOT NULL,
    level_infected boolean NOT NULL,
    emp_id integer NOT NULL
);
 $   DROP TABLE public.rrhh_symptomsemp;
       public         postgres    false    3            �            1259    37678    rrhh_symptomsemp_id_seq    SEQUENCE     �   CREATE SEQUENCE public.rrhh_symptomsemp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.rrhh_symptomsemp_id_seq;
       public       postgres    false    208    3            }	           0    0    rrhh_symptomsemp_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.rrhh_symptomsemp_id_seq OWNED BY public.rrhh_symptomsemp.id;
            public       postgres    false    207            �            1259    37707    security_accessusers    TABLE     �   CREATE TABLE public.security_accessusers (
    id integer NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    hour time without time zone NOT NULL,
    localhost text NOT NULL,
    hostname text NOT NULL,
    user_id integer NOT NULL
);
 (   DROP TABLE public.security_accessusers;
       public         postgres    false    3            �            1259    37705    security_accessusers_id_seq    SEQUENCE     �   CREATE SEQUENCE public.security_accessusers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.security_accessusers_id_seq;
       public       postgres    false    210    3            ~	           0    0    security_accessusers_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.security_accessusers_id_seq OWNED BY public.security_accessusers.id;
            public       postgres    false    209            �            1259    37718    security_company    TABLE     �  CREATE TABLE public.security_company (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    system_name character varying(50) NOT NULL,
    image character varying(100),
    icon character varying(500) NOT NULL,
    ruc character varying(13),
    phone character varying(9),
    mobile character varying(10),
    email character varying(50),
    address character varying(255),
    mission character varying(1000),
    vision character varying(1000),
    about_us character varying(1000),
    layout integer,
    card character varying(50) NOT NULL,
    navbar character varying(50) NOT NULL,
    brand_logo character varying(50) NOT NULL,
    sidebar character varying(50) NOT NULL
);
 $   DROP TABLE public.security_company;
       public         postgres    false    3            �            1259    37716    security_company_id_seq    SEQUENCE     �   CREATE SEQUENCE public.security_company_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.security_company_id_seq;
       public       postgres    false    3    212            	           0    0    security_company_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.security_company_id_seq OWNED BY public.security_company.id;
            public       postgres    false    211            �            1259    37741    security_databasebackups    TABLE     +  CREATE TABLE public.security_databasebackups (
    id integer NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    hour time without time zone NOT NULL,
    localhost character varying(100),
    hostname text,
    archive character varying(100) NOT NULL,
    user_id integer NOT NULL
);
 ,   DROP TABLE public.security_databasebackups;
       public         postgres    false    3            �            1259    37739    security_databasebackups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.security_databasebackups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.security_databasebackups_id_seq;
       public       postgres    false    3    214            �	           0    0    security_databasebackups_id_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.security_databasebackups_id_seq OWNED BY public.security_databasebackups.id;
            public       postgres    false    213            �            1259    37777    security_groupmodule    TABLE     �   CREATE TABLE public.security_groupmodule (
    id integer NOT NULL,
    groups_id integer NOT NULL,
    modules_id integer NOT NULL
);
 (   DROP TABLE public.security_groupmodule;
       public         postgres    false    3            �            1259    37775    security_groupmodule_id_seq    SEQUENCE     �   CREATE SEQUENCE public.security_groupmodule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.security_groupmodule_id_seq;
       public       postgres    false    220    3            �	           0    0    security_groupmodule_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.security_groupmodule_id_seq OWNED BY public.security_groupmodule.id;
            public       postgres    false    219            �            1259    37764    security_module    TABLE     �  CREATE TABLE public.security_module (
    id integer NOT NULL,
    url character varying(100) NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(200),
    icon character varying(100),
    image character varying(100),
    is_vertical boolean NOT NULL,
    is_active boolean NOT NULL,
    is_visible boolean NOT NULL,
    content_type_id integer,
    type_id integer
);
 #   DROP TABLE public.security_module;
       public         postgres    false    3            �            1259    37762    security_module_id_seq    SEQUENCE        CREATE SEQUENCE public.security_module_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.security_module_id_seq;
       public       postgres    false    218    3            �	           0    0    security_module_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.security_module_id_seq OWNED BY public.security_module.id;
            public       postgres    false    217            �            1259    37752    security_moduletype    TABLE     �   CREATE TABLE public.security_moduletype (
    id integer NOT NULL,
    name character varying(150) NOT NULL,
    icon character varying(100) NOT NULL,
    is_active boolean NOT NULL
);
 '   DROP TABLE public.security_moduletype;
       public         postgres    false    3            �            1259    37750    security_moduletype_id_seq    SEQUENCE     �   CREATE SEQUENCE public.security_moduletype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.security_moduletype_id_seq;
       public       postgres    false    3    216            �	           0    0    security_moduletype_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.security_moduletype_id_seq OWNED BY public.security_moduletype.id;
            public       postgres    false    215            �            1259    37577 	   user_user    TABLE     a  CREATE TABLE public.user_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    dni character varying(13) NOT NULL,
    image character varying(100),
    is_change_password boolean NOT NULL,
    token uuid
);
    DROP TABLE public.user_user;
       public         postgres    false    3            �            1259    37594    user_user_groups    TABLE        CREATE TABLE public.user_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.user_user_groups;
       public         postgres    false    3            �            1259    37592    user_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.user_user_groups_id_seq;
       public       postgres    false    198    3            �	           0    0    user_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.user_user_groups_id_seq OWNED BY public.user_user_groups.id;
            public       postgres    false    197            �            1259    37575    user_user_id_seq    SEQUENCE     y   CREATE SEQUENCE public.user_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.user_user_id_seq;
       public       postgres    false    196    3            �	           0    0    user_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.user_user_id_seq OWNED BY public.user_user.id;
            public       postgres    false    195            �            1259    37602    user_user_user_permissions    TABLE     �   CREATE TABLE public.user_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.user_user_user_permissions;
       public         postgres    false    3            �            1259    37600 !   user_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.user_user_user_permissions_id_seq;
       public       postgres    false    3    200            �	           0    0 !   user_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.user_user_user_permissions_id_seq OWNED BY public.user_user_user_permissions.id;
            public       postgres    false    199            F           2604    37536    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    191    192    192            G           2604    37546    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    193    194    194            E           2604    37528    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    190    189    190            K           2604    37643    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    201    202    202            D           2604    37518    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    188    187    188            C           2604    37507    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    186    185    186            M           2604    37667    rrhh_biometric id    DEFAULT     v   ALTER TABLE ONLY public.rrhh_biometric ALTER COLUMN id SET DEFAULT nextval('public.rrhh_biometric_id_seq'::regclass);
 @   ALTER TABLE public.rrhh_biometric ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    204    203    204            N           2604    37675    rrhh_employee id    DEFAULT     t   ALTER TABLE ONLY public.rrhh_employee ALTER COLUMN id SET DEFAULT nextval('public.rrhh_employee_id_seq'::regclass);
 ?   ALTER TABLE public.rrhh_employee ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    205    206    206            O           2604    37683    rrhh_symptomsemp id    DEFAULT     z   ALTER TABLE ONLY public.rrhh_symptomsemp ALTER COLUMN id SET DEFAULT nextval('public.rrhh_symptomsemp_id_seq'::regclass);
 B   ALTER TABLE public.rrhh_symptomsemp ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    207    208    208            P           2604    37710    security_accessusers id    DEFAULT     �   ALTER TABLE ONLY public.security_accessusers ALTER COLUMN id SET DEFAULT nextval('public.security_accessusers_id_seq'::regclass);
 F   ALTER TABLE public.security_accessusers ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    210    209    210            Q           2604    37721    security_company id    DEFAULT     z   ALTER TABLE ONLY public.security_company ALTER COLUMN id SET DEFAULT nextval('public.security_company_id_seq'::regclass);
 B   ALTER TABLE public.security_company ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    211    212    212            R           2604    37744    security_databasebackups id    DEFAULT     �   ALTER TABLE ONLY public.security_databasebackups ALTER COLUMN id SET DEFAULT nextval('public.security_databasebackups_id_seq'::regclass);
 J   ALTER TABLE public.security_databasebackups ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    213    214    214            U           2604    37780    security_groupmodule id    DEFAULT     �   ALTER TABLE ONLY public.security_groupmodule ALTER COLUMN id SET DEFAULT nextval('public.security_groupmodule_id_seq'::regclass);
 F   ALTER TABLE public.security_groupmodule ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    219    220    220            T           2604    37767    security_module id    DEFAULT     x   ALTER TABLE ONLY public.security_module ALTER COLUMN id SET DEFAULT nextval('public.security_module_id_seq'::regclass);
 A   ALTER TABLE public.security_module ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    218    217    218            S           2604    37755    security_moduletype id    DEFAULT     �   ALTER TABLE ONLY public.security_moduletype ALTER COLUMN id SET DEFAULT nextval('public.security_moduletype_id_seq'::regclass);
 E   ALTER TABLE public.security_moduletype ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    215    216    216            H           2604    37580    user_user id    DEFAULT     l   ALTER TABLE ONLY public.user_user ALTER COLUMN id SET DEFAULT nextval('public.user_user_id_seq'::regclass);
 ;   ALTER TABLE public.user_user ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    196    195    196            I           2604    37597    user_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.user_user_groups ALTER COLUMN id SET DEFAULT nextval('public.user_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.user_user_groups ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    197    198    198            J           2604    37605    user_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.user_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.user_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.user_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    200    199    200            O	          0    37533 
   auth_group 
   TABLE DATA               .   COPY public.auth_group (id, name) FROM stdin;
    public       postgres    false    192   �      �	           0    0    auth_group_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_group_id_seq', 3, true);
            public       postgres    false    191            Q	          0    37543    auth_group_permissions 
   TABLE DATA               M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       postgres    false    194   �      �	           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 58, true);
            public       postgres    false    193            M	          0    37525    auth_permission 
   TABLE DATA               N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       postgres    false    190   �      �	           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 54, true);
            public       postgres    false    189            Y	          0    37640    django_admin_log 
   TABLE DATA               �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public       postgres    false    202         �	           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);
            public       postgres    false    201            K	          0    37515    django_content_type 
   TABLE DATA               C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public       postgres    false    188   4      �	           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);
            public       postgres    false    187            I	          0    37504    django_migrations 
   TABLE DATA               C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public       postgres    false    186   �      �	           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 22, true);
            public       postgres    false    185            l	          0    37828    django_session 
   TABLE DATA               P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public       postgres    false    221   �      [	          0    37664    rrhh_biometric 
   TABLE DATA               �   COPY public.rrhh_biometric (id, date_joined, date_joinedtime, hour, "hourEntradaM", "hourSalidaM", "hourEntradaV", "hourSalidaV", "hourExtra", emp_id) FROM stdin;
    public       postgres    false    204   O      �	           0    0    rrhh_biometric_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.rrhh_biometric_id_seq', 3, true);
            public       postgres    false    203            ]	          0    37672    rrhh_employee 
   TABLE DATA               i   COPY public.rrhh_employee (id, dependence, birthdate, cant_familiar, gender, state, user_id) FROM stdin;
    public       postgres    false    206   �      �	           0    0    rrhh_employee_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.rrhh_employee_id_seq', 6, true);
            public       postgres    false    205            _	          0    37680    rrhh_symptomsemp 
   TABLE DATA               �   COPY public.rrhh_symptomsemp (id, date_joined, body_temperature, air_death, dry_cough, intestinal_discomfort, headache, lost_taste, lost_olfato, level_infected, emp_id) FROM stdin;
    public       postgres    false    208   l      �	           0    0    rrhh_symptomsemp_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.rrhh_symptomsemp_id_seq', 10, true);
            public       postgres    false    207            a	          0    37707    security_accessusers 
   TABLE DATA               c   COPY public.security_accessusers (id, date_joined, hour, localhost, hostname, user_id) FROM stdin;
    public       postgres    false    210   �      �	           0    0    security_accessusers_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.security_accessusers_id_seq', 13, true);
            public       postgres    false    209            c	          0    37718    security_company 
   TABLE DATA               �   COPY public.security_company (id, name, system_name, image, icon, ruc, phone, mobile, email, address, mission, vision, about_us, layout, card, navbar, brand_logo, sidebar) FROM stdin;
    public       postgres    false    212   �      �	           0    0    security_company_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.security_company_id_seq', 1, true);
            public       postgres    false    211            e	          0    37741    security_databasebackups 
   TABLE DATA               p   COPY public.security_databasebackups (id, date_joined, hour, localhost, hostname, archive, user_id) FROM stdin;
    public       postgres    false    214   �      �	           0    0    security_databasebackups_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.security_databasebackups_id_seq', 1, false);
            public       postgres    false    213            k	          0    37777    security_groupmodule 
   TABLE DATA               I   COPY public.security_groupmodule (id, groups_id, modules_id) FROM stdin;
    public       postgres    false    220   �      �	           0    0    security_groupmodule_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.security_groupmodule_id_seq', 26, true);
            public       postgres    false    219            i	          0    37764    security_module 
   TABLE DATA               �   COPY public.security_module (id, url, name, description, icon, image, is_vertical, is_active, is_visible, content_type_id, type_id) FROM stdin;
    public       postgres    false    218   )       �	           0    0    security_module_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.security_module_id_seq', 16, true);
            public       postgres    false    217            g	          0    37752    security_moduletype 
   TABLE DATA               H   COPY public.security_moduletype (id, name, icon, is_active) FROM stdin;
    public       postgres    false    216   �"      �	           0    0    security_moduletype_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.security_moduletype_id_seq', 4, true);
            public       postgres    false    215            S	          0    37577 	   user_user 
   TABLE DATA               �   COPY public.user_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, dni, image, is_change_password, token) FROM stdin;
    public       postgres    false    196   #      U	          0    37594    user_user_groups 
   TABLE DATA               A   COPY public.user_user_groups (id, user_id, group_id) FROM stdin;
    public       postgres    false    198   !'      �	           0    0    user_user_groups_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.user_user_groups_id_seq', 7, true);
            public       postgres    false    197            �	           0    0    user_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.user_user_id_seq', 7, true);
            public       postgres    false    195            W	          0    37602    user_user_user_permissions 
   TABLE DATA               P   COPY public.user_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       postgres    false    200   ]'      �	           0    0 !   user_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.user_user_user_permissions_id_seq', 1, false);
            public       postgres    false    199            c           2606    37573    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         postgres    false    192    192            h           2606    37559 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public         postgres    false    194    194    194            k           2606    37548 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         postgres    false    194    194            e           2606    37538    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         postgres    false    192    192            ^           2606    37550 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public         postgres    false    190    190    190            `           2606    37530 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         postgres    false    190    190            �           2606    37649 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         postgres    false    202    202            Y           2606    37522 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public         postgres    false    188    188    188            [           2606    37520 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         postgres    false    188    188            W           2606    37512 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public         postgres    false    186    186            �           2606    37835 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         postgres    false    221    221            �           2606    37669 "   rrhh_biometric rrhh_biometric_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.rrhh_biometric
    ADD CONSTRAINT rrhh_biometric_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.rrhh_biometric DROP CONSTRAINT rrhh_biometric_pkey;
       public         postgres    false    204    204            �           2606    37677     rrhh_employee rrhh_employee_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.rrhh_employee
    ADD CONSTRAINT rrhh_employee_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.rrhh_employee DROP CONSTRAINT rrhh_employee_pkey;
       public         postgres    false    206    206            �           2606    37693 '   rrhh_employee rrhh_employee_user_id_key 
   CONSTRAINT     e   ALTER TABLE ONLY public.rrhh_employee
    ADD CONSTRAINT rrhh_employee_user_id_key UNIQUE (user_id);
 Q   ALTER TABLE ONLY public.rrhh_employee DROP CONSTRAINT rrhh_employee_user_id_key;
       public         postgres    false    206    206            �           2606    37685 &   rrhh_symptomsemp rrhh_symptomsemp_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.rrhh_symptomsemp
    ADD CONSTRAINT rrhh_symptomsemp_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.rrhh_symptomsemp DROP CONSTRAINT rrhh_symptomsemp_pkey;
       public         postgres    false    208    208            �           2606    37715 .   security_accessusers security_accessusers_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.security_accessusers
    ADD CONSTRAINT security_accessusers_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.security_accessusers DROP CONSTRAINT security_accessusers_pkey;
       public         postgres    false    210    210            �           2606    37738 +   security_company security_company_email_key 
   CONSTRAINT     g   ALTER TABLE ONLY public.security_company
    ADD CONSTRAINT security_company_email_key UNIQUE (email);
 U   ALTER TABLE ONLY public.security_company DROP CONSTRAINT security_company_email_key;
       public         postgres    false    212    212            �           2606    37736 ,   security_company security_company_mobile_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.security_company
    ADD CONSTRAINT security_company_mobile_key UNIQUE (mobile);
 V   ALTER TABLE ONLY public.security_company DROP CONSTRAINT security_company_mobile_key;
       public         postgres    false    212    212            �           2606    37728 *   security_company security_company_name_key 
   CONSTRAINT     e   ALTER TABLE ONLY public.security_company
    ADD CONSTRAINT security_company_name_key UNIQUE (name);
 T   ALTER TABLE ONLY public.security_company DROP CONSTRAINT security_company_name_key;
       public         postgres    false    212    212            �           2606    37734 +   security_company security_company_phone_key 
   CONSTRAINT     g   ALTER TABLE ONLY public.security_company
    ADD CONSTRAINT security_company_phone_key UNIQUE (phone);
 U   ALTER TABLE ONLY public.security_company DROP CONSTRAINT security_company_phone_key;
       public         postgres    false    212    212            �           2606    37726 &   security_company security_company_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.security_company
    ADD CONSTRAINT security_company_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.security_company DROP CONSTRAINT security_company_pkey;
       public         postgres    false    212    212            �           2606    37732 )   security_company security_company_ruc_key 
   CONSTRAINT     c   ALTER TABLE ONLY public.security_company
    ADD CONSTRAINT security_company_ruc_key UNIQUE (ruc);
 S   ALTER TABLE ONLY public.security_company DROP CONSTRAINT security_company_ruc_key;
       public         postgres    false    212    212            �           2606    37730 1   security_company security_company_system_name_key 
   CONSTRAINT     s   ALTER TABLE ONLY public.security_company
    ADD CONSTRAINT security_company_system_name_key UNIQUE (system_name);
 [   ALTER TABLE ONLY public.security_company DROP CONSTRAINT security_company_system_name_key;
       public         postgres    false    212    212            �           2606    37749 6   security_databasebackups security_databasebackups_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.security_databasebackups
    ADD CONSTRAINT security_databasebackups_pkey PRIMARY KEY (id);
 `   ALTER TABLE ONLY public.security_databasebackups DROP CONSTRAINT security_databasebackups_pkey;
       public         postgres    false    214    214            �           2606    37782 .   security_groupmodule security_groupmodule_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.security_groupmodule
    ADD CONSTRAINT security_groupmodule_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.security_groupmodule DROP CONSTRAINT security_groupmodule_pkey;
       public         postgres    false    220    220            �           2606    37772 $   security_module security_module_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.security_module
    ADD CONSTRAINT security_module_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.security_module DROP CONSTRAINT security_module_pkey;
       public         postgres    false    218    218            �           2606    37774 '   security_module security_module_url_key 
   CONSTRAINT     a   ALTER TABLE ONLY public.security_module
    ADD CONSTRAINT security_module_url_key UNIQUE (url);
 Q   ALTER TABLE ONLY public.security_module DROP CONSTRAINT security_module_url_key;
       public         postgres    false    218    218            �           2606    37761 0   security_moduletype security_moduletype_icon_key 
   CONSTRAINT     k   ALTER TABLE ONLY public.security_moduletype
    ADD CONSTRAINT security_moduletype_icon_key UNIQUE (icon);
 Z   ALTER TABLE ONLY public.security_moduletype DROP CONSTRAINT security_moduletype_icon_key;
       public         postgres    false    216    216            �           2606    37759 0   security_moduletype security_moduletype_name_key 
   CONSTRAINT     k   ALTER TABLE ONLY public.security_moduletype
    ADD CONSTRAINT security_moduletype_name_key UNIQUE (name);
 Z   ALTER TABLE ONLY public.security_moduletype DROP CONSTRAINT security_moduletype_name_key;
       public         postgres    false    216    216            �           2606    37757 ,   security_moduletype security_moduletype_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.security_moduletype
    ADD CONSTRAINT security_moduletype_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.security_moduletype DROP CONSTRAINT security_moduletype_pkey;
       public         postgres    false    216    216            n           2606    37589    user_user user_user_dni_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_dni_key UNIQUE (dni);
 E   ALTER TABLE ONLY public.user_user DROP CONSTRAINT user_user_dni_key;
       public         postgres    false    196    196            x           2606    37599 &   user_user_groups user_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.user_user_groups DROP CONSTRAINT user_user_groups_pkey;
       public         postgres    false    198    198            {           2606    37611 @   user_user_groups user_user_groups_user_id_group_id_bb60391f_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_user_id_group_id_bb60391f_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.user_user_groups DROP CONSTRAINT user_user_groups_user_id_group_id_bb60391f_uniq;
       public         postgres    false    198    198    198            p           2606    37585    user_user user_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.user_user DROP CONSTRAINT user_user_pkey;
       public         postgres    false    196    196            r           2606    37591    user_user user_user_token_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_token_key UNIQUE (token);
 G   ALTER TABLE ONLY public.user_user DROP CONSTRAINT user_user_token_key;
       public         postgres    false    196    196            ~           2606    37607 :   user_user_user_permissions user_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.user_user_user_permissions DROP CONSTRAINT user_user_user_permissions_pkey;
       public         postgres    false    200    200            �           2606    37625 Y   user_user_user_permissions user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.user_user_user_permissions DROP CONSTRAINT user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq;
       public         postgres    false    200    200    200            u           2606    37587     user_user user_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.user_user DROP CONSTRAINT user_user_username_key;
       public         postgres    false    196    196            a           1259    37574    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public         postgres    false    192            f           1259    37570 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public         postgres    false    194            i           1259    37571 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public         postgres    false    194            \           1259    37556 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public         postgres    false    190            �           1259    37660 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public         postgres    false    202            �           1259    37661 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public         postgres    false    202            �           1259    37837 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public         postgres    false    221            �           1259    37836 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public         postgres    false    221            �           1259    37704    rrhh_biometric_emp_id_ac4c5fc7    INDEX     [   CREATE INDEX rrhh_biometric_emp_id_ac4c5fc7 ON public.rrhh_biometric USING btree (emp_id);
 2   DROP INDEX public.rrhh_biometric_emp_id_ac4c5fc7;
       public         postgres    false    204            �           1259    37691     rrhh_symptomsemp_emp_id_a057d297    INDEX     _   CREATE INDEX rrhh_symptomsemp_emp_id_a057d297 ON public.rrhh_symptomsemp USING btree (emp_id);
 4   DROP INDEX public.rrhh_symptomsemp_emp_id_a057d297;
       public         postgres    false    208            �           1259    37827 %   security_accessusers_user_id_42e83f10    INDEX     i   CREATE INDEX security_accessusers_user_id_42e83f10 ON public.security_accessusers USING btree (user_id);
 9   DROP INDEX public.security_accessusers_user_id_42e83f10;
       public         postgres    false    210            �           1259    37788 $   security_company_email_bedb2ef7_like    INDEX     v   CREATE INDEX security_company_email_bedb2ef7_like ON public.security_company USING btree (email varchar_pattern_ops);
 8   DROP INDEX public.security_company_email_bedb2ef7_like;
       public         postgres    false    212            �           1259    37787 %   security_company_mobile_8d4bc9b2_like    INDEX     x   CREATE INDEX security_company_mobile_8d4bc9b2_like ON public.security_company USING btree (mobile varchar_pattern_ops);
 9   DROP INDEX public.security_company_mobile_8d4bc9b2_like;
       public         postgres    false    212            �           1259    37783 #   security_company_name_988fa227_like    INDEX     t   CREATE INDEX security_company_name_988fa227_like ON public.security_company USING btree (name varchar_pattern_ops);
 7   DROP INDEX public.security_company_name_988fa227_like;
       public         postgres    false    212            �           1259    37786 $   security_company_phone_e047e59a_like    INDEX     v   CREATE INDEX security_company_phone_e047e59a_like ON public.security_company USING btree (phone varchar_pattern_ops);
 8   DROP INDEX public.security_company_phone_e047e59a_like;
       public         postgres    false    212            �           1259    37785 "   security_company_ruc_046aea7e_like    INDEX     r   CREATE INDEX security_company_ruc_046aea7e_like ON public.security_company USING btree (ruc varchar_pattern_ops);
 6   DROP INDEX public.security_company_ruc_046aea7e_like;
       public         postgres    false    212            �           1259    37784 *   security_company_system_name_fd8eaf6e_like    INDEX     �   CREATE INDEX security_company_system_name_fd8eaf6e_like ON public.security_company USING btree (system_name varchar_pattern_ops);
 >   DROP INDEX public.security_company_system_name_fd8eaf6e_like;
       public         postgres    false    212            �           1259    37826 )   security_databasebackups_user_id_e5cb454e    INDEX     q   CREATE INDEX security_databasebackups_user_id_e5cb454e ON public.security_databasebackups USING btree (user_id);
 =   DROP INDEX public.security_databasebackups_user_id_e5cb454e;
       public         postgres    false    214            �           1259    37814 '   security_groupmodule_groups_id_6f1a67f4    INDEX     m   CREATE INDEX security_groupmodule_groups_id_6f1a67f4 ON public.security_groupmodule USING btree (groups_id);
 ;   DROP INDEX public.security_groupmodule_groups_id_6f1a67f4;
       public         postgres    false    220            �           1259    37815 (   security_groupmodule_modules_id_80173609    INDEX     o   CREATE INDEX security_groupmodule_modules_id_80173609 ON public.security_groupmodule USING btree (modules_id);
 <   DROP INDEX public.security_groupmodule_modules_id_80173609;
       public         postgres    false    220            �           1259    37802 (   security_module_content_type_id_3cc35f19    INDEX     o   CREATE INDEX security_module_content_type_id_3cc35f19 ON public.security_module USING btree (content_type_id);
 <   DROP INDEX public.security_module_content_type_id_3cc35f19;
       public         postgres    false    218            �           1259    37803     security_module_type_id_26a24a02    INDEX     _   CREATE INDEX security_module_type_id_26a24a02 ON public.security_module USING btree (type_id);
 4   DROP INDEX public.security_module_type_id_26a24a02;
       public         postgres    false    218            �           1259    37801 !   security_module_url_fabe8c33_like    INDEX     p   CREATE INDEX security_module_url_fabe8c33_like ON public.security_module USING btree (url varchar_pattern_ops);
 5   DROP INDEX public.security_module_url_fabe8c33_like;
       public         postgres    false    218            �           1259    37790 &   security_moduletype_icon_fdf7549f_like    INDEX     z   CREATE INDEX security_moduletype_icon_fdf7549f_like ON public.security_moduletype USING btree (icon varchar_pattern_ops);
 :   DROP INDEX public.security_moduletype_icon_fdf7549f_like;
       public         postgres    false    216            �           1259    37789 &   security_moduletype_name_dc865aa5_like    INDEX     z   CREATE INDEX security_moduletype_name_dc865aa5_like ON public.security_moduletype USING btree (name varchar_pattern_ops);
 :   DROP INDEX public.security_moduletype_name_dc865aa5_like;
       public         postgres    false    216            l           1259    37609    user_user_dni_04964fd1_like    INDEX     d   CREATE INDEX user_user_dni_04964fd1_like ON public.user_user USING btree (dni varchar_pattern_ops);
 /   DROP INDEX public.user_user_dni_04964fd1_like;
       public         postgres    false    196            v           1259    37623 "   user_user_groups_group_id_c57f13c0    INDEX     c   CREATE INDEX user_user_groups_group_id_c57f13c0 ON public.user_user_groups USING btree (group_id);
 6   DROP INDEX public.user_user_groups_group_id_c57f13c0;
       public         postgres    false    198            y           1259    37622 !   user_user_groups_user_id_13f9a20d    INDEX     a   CREATE INDEX user_user_groups_user_id_13f9a20d ON public.user_user_groups USING btree (user_id);
 5   DROP INDEX public.user_user_groups_user_id_13f9a20d;
       public         postgres    false    198            |           1259    37637 1   user_user_user_permissions_permission_id_ce49d4de    INDEX     �   CREATE INDEX user_user_user_permissions_permission_id_ce49d4de ON public.user_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.user_user_user_permissions_permission_id_ce49d4de;
       public         postgres    false    200                       1259    37636 +   user_user_user_permissions_user_id_31782f58    INDEX     u   CREATE INDEX user_user_user_permissions_user_id_31782f58 ON public.user_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.user_user_user_permissions_user_id_31782f58;
       public         postgres    false    200            s           1259    37608     user_user_username_e2bdfe0c_like    INDEX     n   CREATE INDEX user_user_username_e2bdfe0c_like ON public.user_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.user_user_username_e2bdfe0c_like;
       public         postgres    false    196            �           2606    37565 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public       postgres    false    2144    190    194            �           2606    37560 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public       postgres    false    194    192    2149            �           2606    37551 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public       postgres    false    2139    190    188            �           2606    37650 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public       postgres    false    188    202    2139            �           2606    37655 B   django_admin_log django_admin_log_user_id_c564eba6_fk_user_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_user_user_id;
       public       postgres    false    202    196    2160            �           2606    37699 A   rrhh_biometric rrhh_biometric_emp_id_ac4c5fc7_fk_rrhh_employee_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.rrhh_biometric
    ADD CONSTRAINT rrhh_biometric_emp_id_ac4c5fc7_fk_rrhh_employee_id FOREIGN KEY (emp_id) REFERENCES public.rrhh_employee(id) DEFERRABLE INITIALLY DEFERRED;
 k   ALTER TABLE ONLY public.rrhh_biometric DROP CONSTRAINT rrhh_biometric_emp_id_ac4c5fc7_fk_rrhh_employee_id;
       public       postgres    false    206    204    2186            �           2606    37694 <   rrhh_employee rrhh_employee_user_id_b2f39fbc_fk_user_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.rrhh_employee
    ADD CONSTRAINT rrhh_employee_user_id_b2f39fbc_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;
 f   ALTER TABLE ONLY public.rrhh_employee DROP CONSTRAINT rrhh_employee_user_id_b2f39fbc_fk_user_user_id;
       public       postgres    false    206    2160    196            �           2606    37686 E   rrhh_symptomsemp rrhh_symptomsemp_emp_id_a057d297_fk_rrhh_employee_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.rrhh_symptomsemp
    ADD CONSTRAINT rrhh_symptomsemp_emp_id_a057d297_fk_rrhh_employee_id FOREIGN KEY (emp_id) REFERENCES public.rrhh_employee(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.rrhh_symptomsemp DROP CONSTRAINT rrhh_symptomsemp_emp_id_a057d297_fk_rrhh_employee_id;
       public       postgres    false    206    208    2186            �           2606    37821 J   security_accessusers security_accessusers_user_id_42e83f10_fk_user_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.security_accessusers
    ADD CONSTRAINT security_accessusers_user_id_42e83f10_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.security_accessusers DROP CONSTRAINT security_accessusers_user_id_42e83f10_fk_user_user_id;
       public       postgres    false    210    196    2160            �           2606    37816 R   security_databasebackups security_databasebackups_user_id_e5cb454e_fk_user_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.security_databasebackups
    ADD CONSTRAINT security_databasebackups_user_id_e5cb454e_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;
 |   ALTER TABLE ONLY public.security_databasebackups DROP CONSTRAINT security_databasebackups_user_id_e5cb454e_fk_user_user_id;
       public       postgres    false    214    2160    196            �           2606    37804 M   security_groupmodule security_groupmodule_groups_id_6f1a67f4_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.security_groupmodule
    ADD CONSTRAINT security_groupmodule_groups_id_6f1a67f4_fk_auth_group_id FOREIGN KEY (groups_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.security_groupmodule DROP CONSTRAINT security_groupmodule_groups_id_6f1a67f4_fk_auth_group_id;
       public       postgres    false    192    2149    220            �           2606    37809 S   security_groupmodule security_groupmodule_modules_id_80173609_fk_security_module_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.security_groupmodule
    ADD CONSTRAINT security_groupmodule_modules_id_80173609_fk_security_module_id FOREIGN KEY (modules_id) REFERENCES public.security_module(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.security_groupmodule DROP CONSTRAINT security_groupmodule_modules_id_80173609_fk_security_module_id;
       public       postgres    false    2228    218    220            �           2606    37791 E   security_module security_module_content_type_id_3cc35f19_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.security_module
    ADD CONSTRAINT security_module_content_type_id_3cc35f19_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.security_module DROP CONSTRAINT security_module_content_type_id_3cc35f19_fk_django_co;
       public       postgres    false    218    188    2139            �           2606    37796 J   security_module security_module_type_id_26a24a02_fk_security_moduletype_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.security_module
    ADD CONSTRAINT security_module_type_id_26a24a02_fk_security_moduletype_id FOREIGN KEY (type_id) REFERENCES public.security_moduletype(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.security_module DROP CONSTRAINT security_module_type_id_26a24a02_fk_security_moduletype_id;
       public       postgres    false    2225    218    216            �           2606    37617 D   user_user_groups user_user_groups_group_id_c57f13c0_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_group_id_c57f13c0_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.user_user_groups DROP CONSTRAINT user_user_groups_group_id_c57f13c0_fk_auth_group_id;
       public       postgres    false    2149    192    198            �           2606    37612 B   user_user_groups user_user_groups_user_id_13f9a20d_fk_user_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_user_id_13f9a20d_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.user_user_groups DROP CONSTRAINT user_user_groups_user_id_13f9a20d_fk_user_user_id;
       public       postgres    false    2160    198    196            �           2606    37631 S   user_user_user_permissions user_user_user_permi_permission_id_ce49d4de_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permi_permission_id_ce49d4de_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.user_user_user_permissions DROP CONSTRAINT user_user_user_permi_permission_id_ce49d4de_fk_auth_perm;
       public       postgres    false    190    200    2144            �           2606    37626 V   user_user_user_permissions user_user_user_permissions_user_id_31782f58_fk_user_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_user_id_31782f58_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.user_user_user_permissions DROP CONSTRAINT user_user_user_permissions_user_id_31782f58_fk_user_user_id;
       public       postgres    false    196    2160    200            O	   1   x�3�tL����,.)JL�/�2�t�-�I���9�KR��@y�=... V)      Q	   �   x�л�1Q{:�=�}ry�Ǳ�3堋4������R�P�'mb����H+݊�G�@�S@�R`e(��
�L\�/�x�d�
�,�U�xU2^��W[ƫ#�Օ��)�z�ס�k+�:�x]������*��w��G��,jU�T��*���Uӹ5��Mg�Й�t�m��[��M�o�7��o���x���f���ߟ��?/      M	   `  x�m�K��0���)8�hx�c��D��&�2R���aH�Ǌr��X�]��ڽk����?�j�T�f��fz\�ȅ[�pk���G��j�jF�-K������w�ö���l���YۙQ^7��1�{�~�AP��ޑp���:�u���e�L��9x�S��� �D�[�q�4f\ܷ˖ۤE�E`kۑyEu�`�b|M��xPd�E�h����nmu������OT�ܱ3uD�"V<�B�jGrD>4��f{j��U͝�@��ĮV�V}��h�T��y5ä��vJ�'r�92!_��T�랝�|���jQe�E5���=�%Ml_6	�~��$�7����?8����]{#��=�q�o�`���p�4��3M�I��jS�*J�}�ܔ��,Y���ʒu���,�=�X���m^����X%�em��Yb�u^��E��{'��ۿ��CAo�e��/�d X�E�A�/�{�p���i�z�ZgX���i-+�z$Y�Q��$MG9o�N��n\̠��ކ�X���G��}4���Q(6!	�ddEB/� N�Kg��]���ؗ�#k6;�w�	�08��G�+�ߟ���`�      Y	      x������ � �      K	   �   x�]�I� е}��d�p�n�Ԁ��/%�Ru����lzv����v�sZ!PtVĲ�~�%r8�a�jk*����#�	9
����hSmL�,�'vA����f����&m�9>���7j����Q��ڵ�w���T=ĸ�@.l\���R\H����&ˎR�_D� �'h�      I	   �  x���ݎ� �����$b��<K%�� ���6o_�Y�v�:7ܘ��̙��9}t}���M!��}��m� ��G������H$L�	��7%���Ù�����vnTJ�E;��vqd���*��6�`F:?M~�KE��OӺ��n���R���+��I��Y�nB4�Bd���L�G�f㴊`��⧬��h�M;\|�kn�}aDQ^�P"�2~�>�m�5���:E�]��ȇm���!Lƞ�ƅ0ӹi��b,��M�8�j͆���@%�o���E��䎺�a��Iq����yL93�������HF�lX���?�LKV$)�����)��h�C�9O)���`�C^�*D�$@D> �ə����ޯ�^��:�Ӌ`(
Z�SM�7^��\�"�U�K��~�%i����Z	9*9�$"i&w�����-2&4,C#�%{��DJ�G���0lVDk,ş��n���4      l	   a  x��M��F��3�"�hGn3x�=؀<�	�_�����n0c�_�23m�S��vu�[oW=H��Ȯ����9�f���]>���[��I�?�U-�a7PA:�׊-�n�B��*Ten"ٮU��g.+��*�t�
K=�?~+�{_wv(�(�E��6O��0kOt{�ae4����P"�}([�/<{���:f��YKe�MWVCK�HC���aS�+��y'�*��v̽@�=.T���Vas���}aWlA:&"��l�eO\2���
}H��R&�Ra�Z%U��t��!�r��s��z�{�=�Xvx�"-���z�v�`�n�[[���5�ug:�uMùW4{���^�v�JgY�@�H/���/��VwM���Kb�f��L�[�nմ�t0a�x�������|y6�nKġ���K���i�\���է�Z�
�Od~��|.i�|2�_B��~h�n��p~M��Ŋ%%���}@�]���W6���G����Z���:�
����\�P�%��9��w�?}��(��legT�7��s���I�O��9�D��<
���6':ԋǷ/�>�t�k}�"Wа��y�gi~�cX/���V+���ҷ��|�mY闚�v�ޥ���7x"P�b/�?z��k�z�Cn�=7��߿c����{�5�� �BA���S�z�{by�rQ$�����Q�
&�w�K� M����.��u��񬠊Ӥ"��u��6�-��:��AUb�*���&��F�c�[(��G^���c]�O�M��ٲ�&���I�d�4���_$���&�e�M�H�s�����5;�	R�CJ�͆H=����':%@�o
g��-JZ�`� K@�8u�]�v�H��{���%{��?��py��?
�Q?�� ˿ 4}�H��L��ǥ�4(~�VSM��e�v7I����=���Uo����k0�ة����C�U	���vecS������W~��;�A��g�YÂ[;Q��>���A�!�<� + �4��Y��EZ���C~��'���Jo�
�>x��X!�M&o���u���:%i�H���%��n�)��쬠��"��,����b򦼾)�$k#,~y~~��X��      [	   o   x�u��� �\6 �[D����C?&<f.a���c�,\kL�,h2��Ӈ 7�����T8[�E5V�B*�eQ�����Ŀ����VR�:>�˳)�D��H,7      ]	   �   x�e�[�0���3{���^L�k�RY��1���?�AҘ������Fq����m�9�@HPbSX�W�f�M\�Ic�yI!M��Hq,�M[�U[�{̵e���
3��~OX��P6�}���׹�Q�`�RK�� ��@�      _	   @   x���4202�50�5��44�4BY�i�e�,ob���0�L�� )06�K��q��qqq ��      a	     x��ҿj�0���z������Nnv h
-��t�P(�Cߟ*F�*����#���h1ZNJ*Y%A�(Ӿ'�H �������l���q>�����$���!6������hk7Z�;ȣ��p��ڣE�Q�(���hO�R�blN�ў����H�����hQ� feW�Uh�Ѣ�A�UڞZ�5��r�� pcj��mN>`T)���BYs��w#PA��?���_DoO)�ٝn��*'��i9��=�\O-���j=����k��y      c	   �   x�}�;�0E�Ud��+�����<H��	aB��Ջ3�X؝s�I�d:�itmX��"�8�#�CpC�8�!��!�gRf�,ˢ(���q�E/2��ޑ�̏7,���pV�;�w'�������ϼA��*�����Ia�U4x��g�q��G
����sm:��[���*c��U�      e	      x������ � �      k	   g   x���1�&�-�,y&��?��Ow����"d6��Y��6�u��|�m=���ZJ�,�3ة��ג�����*���Z�|����긡���{[      i	   g  x�ŕ;��0�k�����sw������n���&L�����X��(��K��"�k�fHjĸG�;�M���i�/k,���h�x���K��l�\I�e�J�)�Y�������+�jc\e,6�����F�����nQ¦R�֘!�wD�(kg��쳋�b�.������eX��|&M4�@����^��뉘��:$U�aȼ9��� K�ȗ ���z��AuY�����O���5S�(���*����x����}H��	G�����P�fe�!�oM�,���c.�T�l֙��&����H���ꡋf4A*u4 hU�cιM�L���1�����O�m!oKG}�+X����¡���k��ߨc��sh��-x�Ӹ�2��:���B��Rn4�У��cl��Z�t0NYάd:~�j	��8Zx�:�u1��f�Q[ev�0�pmsJ�Ys�xU�~��&lZP ��6�)Dn�w�����MOl?P����`��XK�w4M�&��LM;SKi4'���{���N��
-����eĶ�0Kfg�>�#���;�ƅ��LtR?���{��섵̟��ݠc�Be%n�i�x(��/�y��      g	   _   x�3�NM/-�LIL�LK,VHK���O��,�2�-.M,��/�I��e�9Sr3�2�K��3o΃)(���)0�
��@֦�55F��� �%�      S	     x����n�H�����w���]��R��%����4*�e�16���M_��<E^l�,��F=�,���~�W�����
#��n�0�U$�y��i�/��>�EUF�f0�K&�S<n���������vM������\��0�І�����D5�(������4���j�|�S޿����ځP�Ƿ&I�.�*N� _��}a!Qc������C��DJ@0E�A���6X�*d��Xc�$F|��*����Uu�ޒ�Á�I�\��ܿu�K8~I���Իm�������u{�A��H �ܜW�!ά�*S�σ���Z�G���k��	=������ڟ�M+ue0Mm�2aS���5��@D�iQ!��S�9jz�__��r��6!|�	�}w��E7�L:;Z_��=/ڸ�l�z�_�Gz����dK$$���j�,�)�(�sn��q��@�c����M��tt�3���5,�C�<J6��J-(m_+hSl��1U6���؜��z��=T�J�Z��uX}�����[�($ڋZ�r����Eo��&|��i
��]쾀o�GB�9K�:�<^�L�a,Uh3�#�V�R��YB���}�4���^��I۴�@��@�DS)}3�adS��\�#N*�4dQ>�Yc [wlR��������������J��<)��r���n�hu�v�i~@J�k�.K�Y�,,^�܁�.��5V�B�9H6��7.\��A��C״2䇆%��f~%r͟��( ʇD	�a���Qژg7��V�IK�����&ݎ�+��:�OWw�|B�o��b�H&uN? ]ff�7U����P�V���4xS��[+�Vo�o(�q�:�W��U��աo&���<!�-�	-VBj�Y��_qOSzb�c���d�N;Y��<x����D�I=ϿN/��x�<6�����~I)�VCء.�'�X@�Mc�*�z�(w��=����g���uZCܑ���C�hq����qr��dK�$:���!17A�oN�R���1      U	   ,   x���	 0��l1�W3鿎,A�bJ�����e�;�>�r�      W	      x������ � �     