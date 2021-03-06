
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
"
" " let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

Plugin 'Valloric/YouCompleteMe'

call vundle#end()

filetype plugin indent on
set backspace=2         " backspace in insert mode works like normal editor
syntax on               " syntax highlighting
filetype indent on      " activates indenting for files
set autoindent          " auto indenting
set number              " line numbers
set ruler               "Always show current position

" Show partial commands in the last line of the screen
 set showcmd

" Configure backspace so it acts as it should act
set backspace=eol,start,indent
set whichwrap+=<,>,h,l

" In many terminal emulators the mouse works just fine, thus enable it.
if has('mouse')
  set mouse=a
endif

" Ignore case when searching
set ignorecase

" Highlight search results
set hlsearch
highlight Search ctermbg=cyan
highlight Pmenu ctermfg=black ctermbg=grey 
highlight PmenuSel ctermfg=black ctermbg=grey 

" Show matching brackets when text indicator is over them
set showmatch

" Enable syntax highlighting
syntax enable

" Be smart when using tabs ;)
set smarttab

" 1 tab == 4 spaces
set shiftwidth=4
set tabstop=4
set expandtab

" solarized theme
syntax enable
"set background=dark
"colorscheme solarized

"    " Display filename
"set laststatus=2
"set statusline+=%F
set title

nnoremap d "_d
vnoremap d "_d

set completeopt-=preview
"
let g:ycm_autoclose_preview_window_after_completion=1
let g:ycm_complete_in_comments=1
let g:ycm_min_num_of_chars_for_completion=1
let g:ycm_confirm_extra_conf=0
let g:ycm_python_binary_path='/usr/bin/python3'
set clipboard=unnamed
