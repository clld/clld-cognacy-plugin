<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "cognatesets" %>
<%block name="title">${_('Cognateset')} ${ctx.name}</%block>

<h2>${_('Cognateset')} ${ctx.name}</h2>

% if ctx.description:
<p>${ctx.description}</p>
% endif

% if map_ or request.map:
${(map_ or request.map).render()}
% endif

<ul>
% for co in ctx.cognates:
<li>${h.link(request, co.counterpart)}</li>
% endfor
</ul>
