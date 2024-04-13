import collections

def fn_counter():
    k1 = 'Vercel (formerly Zeit Now): Vercel is another platform for deploying web applications, particularly popular for serverless applications and static sites. Like Heroku and Netlify, you can connect your GitHub repository to Vercel and set up automatic deployments.'
    print(collections.Counter(k1))

def ordered_dct():
    dct = {}
    dct['a'] = 1
    dct['b'] = 2
    dct['c'] = 3
    odct = collections.OrderedDict({'a':1, 'b':2, 'c':3})
    print(dct)
    print(odct)

ordered_dct()