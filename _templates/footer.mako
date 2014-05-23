<% import datetime %>
<footer>
  <div id="footer" class="grid_12">
    <div class="grid_8">
      <p>
        <a href="${bf.util.site_path_helper(bf.config.blog.path,'feed','index.xml')}">RSS das Postagens</a>
        % if bf.config.blog.disqus.enabled:
        <a href="http://${bf.config.blog.disqus.name}.disqus.com/latest.rss">RSS dos Coment&aacute;rios</a>.
        % endif
      </p>
    </div>
    <div class="grid_4" id="credits">
      <p>
        Copyleft ${datetime.datetime.now().year}
        ${bf.config.site.author}
      </p>
      <p>
        Este blog utiliza <a href="http://www.blogofile.com">Blogofile</a> e está hospedado em <a href="http://tem.blog.br">Tem.Blog.BR</a>.
      </p>
    </div>
  </div>
</footer>
