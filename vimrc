syntax on
set tabstop=4
set shiftwidth=4
set softtabstop=4
set autoindent 
set smartindent
set termguicolors
colorscheme peachpuff
set number
set mouse=a
let mapleader = " "

" Specify a directory for plugins
call plug#begin('~/.vim/plugged')


" LSP and completion plugin
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'voldikss/vim-floaterm'
Plug 'prabirshrestha/vim-lsp'
Plug 'mattn/vim-lsp-settings'
Plug 'preservim/nerdtree'
Plug 'preservim/nerdcommenter'
" Initialize plugin system
call plug#end()

function! s:on_lsp_buffer_enabled() abort
	setlocal omnifunc=lsp#complete
endfunction

augroup lsp_install
	au!
	autocmd user lsp_buffer_enabled call s:on_lsp_buffer_enabled()
augroup END


" Key mappings for CoC.nvim
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gi <Plug>(coc
"Key mappign for floaterm
let g:floaterm_keymap_new = '<Leader>ft'
let g:floaterm_keymap_toggle = '<Leader>t'
"Key mapping for nerdTree
nnoremap <leader>nt :NERDTreeToggle<CR>
"Copy and Paste Stuff
vnoremap <C-c> "+y
map <C-p> "+p
