# -*- coding: utf-8 -*-

######################################################################
# Configuração para tem.blog.br
# Baseada na configuração padrão de www.blogofile.com
#
# Edite isto ANTES de pedir pra botar o site no ar.
#
######################################################################

## site_url -- URL do site.
#
# Aqui deve necessariamente constar um URL no formato:
# http://alguem.tem.blog.br OU https://alguem.tem.blog.br
#
# Altere 'alguem' pelo nome do teu site (ou deixe assim, se ninguém ainda
# tiver registrado o sub domínio 'alguem', tu pode ser x primeirx.
# PS: Ah, lembrei que 'ninguém' já tem blog em http://ninguem.tem.blog.br
#
# A parte '.tem.blog.br' deve ficar exatamente desta forma.
#
# Tu pode usar https:// ao invés de http:// para forçar o protocolo
# seguro, mas leve em consideração que o domínio tem.blog.br usa
# certificados da cacert.org, que podem exibir telas vermelhas em alguns
# navegadores desatualizados.
#
site.url = "http://alguem.tem.blog.br"

## site.author -- Nome dx autorx do site.
#
# Isto é opcional. Se deixado em branco "" o site fica sem autor/x.
#
# Caso alguma coisa seja colocada entre as aspas, então todo lugar onde
# o site gera nome de autor vai ficar com este nome aqui.
#
site.author = ""

#### Configurações do blog ####
#
# Só altere estas configurações se souber o que está fazendo. Se eu
# achar que tem alguma configuração que vai resultar em erro, não vou
# botar o teu site no ar.
#
# De fato, eu te incentivo a aprender sobre as configurações do blogofile
# e mexer aqui pra customizar teu site. Senão, serão todos sites iguais.
#
blog = plugins.blog
blog.enabled = True
blog.timezone = "America/Sao_Paulo"
site.file_ignore_patterns = [
".*/_.*",
".*/#.*",
".*~$",
".*/\..*\.swp$",
".*/\.(git|hg|svn|bzr)$",
".*/.(git|hg)ignore$",
".*/CVS$",
]
blog.auto_permalink.enabled = True
blog.auto_permalink.path = ":blog_path/:year/:month/:day/:title"
blog.custom_index = False
blog.post_excerpts.enabled = False
blog.post_default_filters = {
    "markdown": "syntax_highlight, markdown",
    "textile": "syntax_highlight, textile",
    "org": "syntax_highlight, org",
    "rst": "syntax_highlight, rst",
    "html": "syntax_highlight"
}
filters.markdown.extensions.def_list.enabled = True
filters.markdown.extensions.abbr.enabled = True
filters.markdown.extensions.footnotes.enabled = True
filters.markdown.extensions.fenced_code.enabled = True
filters.markdown.extensions.headerid.enabled = True
filters.markdown.extensions.tables.enabled = True
blog.template_path = "_templates/blog"
### Fim das configurações do blog ###

## blog_path -- Diretório do blog.
#
# Este é o caminho onde ficam as páginas do blog.
#
# Por exemplo, por padrão a primeira publicação ficaria em
# http://alguem.tem.blog.br/blog/tenho_blog
#
blog.path = "/blog"

## blog.posts_per_page -- Número de posts por página
blog.posts_per_page = 1


## blog_name -- Nome do blog.
blog.name = "Alguém Tem Blog .BR"

## blog_description -- Descrição do blog. Aparece no feed RSS.
blog.description = "Não tem blog? Aqui, \"alguém\" tem blog!"

## Disqus
#
# Crie uma conta em disqus.com para ter comentários no blog. Disqus é uma
# empresa comercial. Use o serviço por tua conta e risco. Mais instruções
# em http://ninguem.tem.blog.br/tutorial/disqus
#
# Para não usar isto, troque 'True' para 'False' e remova ou comente a
# linha blog.disqus.name
#
blog.disqus.enabled = True
blog.disqus.name = "alguemtemblogbr"

## blog_googleanaltics_id -- ID do Google Analytics
#blog.googleanlytics_id = "UA-XXXXX-X"

