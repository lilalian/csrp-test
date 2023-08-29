"""---
title: "CSRP"
pagetitle: CSRP – Center for Suicide Prevention and Research
page-layout: custom
section-divs: false
css: index.css
toc: false
image: https://nbdev.fast.ai/images/card.png
description: Novel implementation strategies for improved suicide prevention efforts
---"""


from fastcore.foundation import L
from nbdev import qmd

def img(fname, classes=None, **kwargs): return qmd.img(f"images/{fname}", classes=classes, **kwargs)
# def btn(txt, link): return qmd.btn(txt, link=link, classes=['btn-action-primary', 'btn-action', 'btn', 'btn-success', 'btn-lg'])
def banner(txt, classes=None, style=None): return qmd.div(txt, L('hero-banner')+classes, style=style)


# def industry(im, **kwargs): return qmd.div(img(im, **kwargs), ["g-col-12", "g-col-sm-6", "g-col-md-3"])

# def testm(im, nm, detl, txt):
#     return qmd.div(f"""{img(im, link=True)}

# {nm}

## {detl}

### {txt}""", ["testimonial", "g-col-12", "g-col-md-6"])

# expert_d = qmd.div('\n'.join(testms.starmap(testm)), ['content-block', 'grid', 'gap-4'])

# def feature(im, desc): return qmd.div(f"{img(im+'.svg')}\n\n{desc}\n", ['feature', 'g-col-12', 'g-col-sm-6', 'g-col-md-4'])

# feature_d = qmd.div('\n'.join(features.starmap(feature)), ['grid', 'gap-4'], style={"padding-bottom": "60px"})

def b(*args, **kwargs): print(banner (*args, **kwargs))
# def d(*args, **kwargs): print(qmd.div(*args, **kwargs))

###
# Output section
###

b(f"""# <span style='color:#009AF1'>SUICIDE RISK PREVENTION</span><br> AND RESEARCH

### Novel implementation strategies for improved suicide prevention efforts

{img('https://nbdev.fast.ai/images/card.png', style={"margin-top": "40px", "margin-bottom": "40px"}, link=True)}""", "content-block")


