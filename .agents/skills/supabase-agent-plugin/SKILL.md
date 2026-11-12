# Supabase agent plugin integration

Upstream: https://github.com/supabase-community/supabase-plugin

## Verification and scope
The upstream GitHub README was inspected on 2026-11-12. This is a locally authored PuteraMY integration guide, **not** an installed copy of the upstream software, MCP server or complete skills. Check the current upstream docs, license and compatibility before installing or running anything.

## When and how to use
For Supabase-backed apps, consult the official Supabase agent plugin for product guidance, Postgres best practices and MCP integration. The official plugin provides MCP plus skills but must be installed and authorized in the target agent separately. Inspect current schema, migrations, RLS, auth, policies, storage and secrets; use migrations and staging-first verification. Never change production schema or permissions without approval. Avoid duplicate MCP registrations.

## Quality gates
1. Inspect existing project instructions, code and environment.
2. Confirm tool availability and required authorization.
3. Pick a narrow, reversible workflow and preserve working behavior.
4. Execute appropriate checks and collect actual evidence.
5. Report commands run, results, known limitations and outstanding work. Never fabricate verification.

## Production safety
No destructive actions, secret exposure, security attacks, or production deployment without explicit approval.
