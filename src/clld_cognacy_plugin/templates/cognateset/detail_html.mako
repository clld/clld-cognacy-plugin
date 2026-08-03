<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! from clld_cognacy_plugin.models import Cognate %>
<%! active_menu_item = "cognatesets" %>
<%block name="title">${_('Cognateset')} ${ctx.name}</%block>

<h2>${_('Cognateset')} ${ctx.name}</h2>

% if ctx.description:
<p>${ctx.description}</p>
% endif

% if map_ or request.map:
${(map_ or request.map).render()}
% endif

<% dt = request.get_datatable('cognates', Cognate, cognateset=ctx) %>
% if dt:
<div>
    ${dt.render()}
</div>
% endif
