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
Plug 'voldikss/vim-floaterm'
Plug 'prabirshrestha/vim-lsp'
Plug 'mattn/vim-lsp-settings'
Plug 'preservim/nerdtree'
Plug 'preservim/nerdcommenter'
Plug 'ojroques/vim-oscyank'
" Initialize plugin system
call plug#end()


" Normal mode: copy the current line to the clipboard
nmap <leader>y <Plug>OSCYank

" Visual mode: copy the selected text to the clipboard
vmap <leader>y <Plug>OSCYankVisual

" Example to copy the whole buffer
nmap <leader>Y :%OSCYank<CR>

function! s:on_lsp_buffer_enabled() abort
        setlocal omnifunc=lsp#complete
endfunction

augroup lsp_install
        au!
        autocmd user lsp_buffer_enabled call s:on_lsp_buffer_enabled()
augroup END


"Key mappign for floaterm
let g:floaterm_keymap_new = '<Leader>ft'
let g:floaterm_keymap_toggle = '<Leader>t'
"Key mapping for nerdTree
nnoremap <leader>nt :NERDTreeToggle<CR>
""Copy and Paste Stuff
"vnoremap <C-c> "+y
"vnoremap <C-p> "+p

