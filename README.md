# 🤖 EduBot - School Helpdesk Chatbot

A responsive web-based chatbot designed to assist students with common school-related inquiries. Built with HTML, CSS, and JavaScript, featuring a modern UI and intelligent response system.

## 🌟 Features

- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Modern UI**: Glass-morphism effects, smooth animations, and gradient backgrounds
- **Smart Responses**: Pattern-matching algorithm to understand user queries
- **Quick Actions**: Pre-defined buttons for common questions
- **Typing Indicators**: Realistic chat experience with animated typing dots
- **Multiple Topics**: Handles queries about library, schedules, food, parking, and more

## 🚀 Live Demo

[View Live Demo](https://yourusername.github.io/school-chatbot) *(Update this link after deployment)*

## 📸 Screenshots

### Desktop View
![Desktop Screenshot](screenshots/desktop-view.png)

### Mobile View
![Mobile Screenshot](screenshots/mobile-view.png)

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Design**: CSS Grid, Flexbox, CSS Animations
- **Development**: Visual Studio Code, Live Server
- **Version Control**: Git, GitHub

## 📋 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/school-chatbot.git
   cd school-chatbot
   ```

2. **Open with Live Server**
   - Install VS Code Live Server extension
   - Right-click on `index.html`
   - Select "Open with Live Server"

3. **Or open directly in browser**
   ```bash
   open index.html
   ```

## 🎯 Usage

1. **Web Version**: Open `index.html` in any modern browser
2. **Python Version**: Run `python chatbot.py` in terminal
3. **Interact**: Type messages or click quick action buttons
4. **Topics**: Ask about library hours, schedules, food, parking, etc.

## 🔧 Customization

### Adding New Topics
1. **Add keywords** to the `patterns` object in `script.js`:
   ```javascript
   newTopic: ['keyword1', 'keyword2', 'keyword3']
   ```

2. **Add responses** to the `responses` object:
   ```javascript
   newTopic: [
       "Response 1 with emoji 🎯",
       "Response 2 with emoji 📚",
       "Response 3 with emoji ✨"
   ]
   ```

3. **Add quick button** (optional):
   ```html
   <button class="quick-button" onclick="sendQuickMessage('Your topic')">
       🎯 Your Topic
   </button>
   ```

### Styling Customization
- **Colors**: Modify gradient values in CSS
- **Animations**: Adjust keyframe animations
- **Layout**: Change flexbox and grid properties

## 📊 Performance Features

- **Lightweight**: No external dependencies
- **Fast Loading**: Optimized CSS and JavaScript
- **Smooth Animations**: 60fps animations with CSS transforms
- **Memory Efficient**: Stores data in memory only

## 🔮 Future Enhancements

- [ ] Voice recognition integration
- [ ] Multi-language support  
- [ ] AI/ML integration (OpenAI API)
- [ ] Database storage for conversations
- [ ] Admin panel for managing responses
- [ ] File upload capability
- [ ] Email integration
- [ ] Push notifications

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Inspired by modern chat applications
- Icons from emoji unicode standard
- Color palette inspired by modern design trends

## 📈 Project Stats

- **Lines of Code**: ~500
- **File Size**: ~15KB
- **Load Time**: <100ms
- **Browser Support**: Chrome, Firefox, Safari, Edge

---

⭐ **Star this repository if you found it helpful!**